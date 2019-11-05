"""
regsys_api.authsys Views Configuration
"""
from rest_framework.response import Response
from django.db import transaction
from rest_framework.views import (APIView)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import status
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
#from django.views.decorators.debug import sensitive_post_parameters

from .models import (
    User,
    RegistrationHandler,
    ForgotPasswordHandler
)

from .serializers import (
    UserSerializer,
    LoginRequestSerializer,
    RegistrationRequestSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmationRequestSerializerPost,
    PasswordChangeRequestSerializer,
    EmailConfirmationSerializer,
    UpdateProfileSerializer
)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


class GetCurrentUserView(APIView):
    """
    Provides the ability to get a user information
    """

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    def get(self, request):
        if(request.user.is_anonymous):
            return Response()
        response_serializer = UserSerializer(request.user)
        return Response(data=response_serializer.data)


class LoginView(APIView):
    """
    Provides the ability to login as a user with a username and password
    """

    serializer_class = LoginRequestSerializer

    ###@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    # @method_decorator(sensitive_post_parameters('password'))
    def post(self, request):
        request_serializer = LoginRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=request_serializer.validated_data['email'].lower(),
            password=request_serializer.validated_data['password']
        )

        if user is None:
            return Response(
                {
                    'message': 'User email or password is incorrect.',
                    'status': 'failed',
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_confirmed:
            return Response(
                {
                    'message': 'User email hasn\'t been confirmed.',
                    'status': 'failed'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)

        user.last_login = timezone.now()
        user.save()

        response_serializer = UserSerializer(request.user)
        return Response(data=response_serializer.data)


class LogoutView(APIView):
    """
    Provides the ability to logout as a user
    """
    permission_classes = (IsAuthenticated,)

    ##@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    # @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(never_cache)
    def post(self, request):
        logout(request)
        return Response()


class RegistrationView(APIView):
    """
    Provides the ability to register as a new user with a username, full name and password
    """

    serializer_class = RegistrationRequestSerializer

    ##@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    # @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(never_cache)
    def post(self, request):
        request_serializer = RegistrationRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = User.objects.create_user(
                email=request_serializer.validated_data['email'].lower(),
                password=request_serializer.validated_data['password'],
                full_name=request_serializer.validated_data['full_name']
            )

            attempt = RegistrationHandler.objects.create(user=user)
            attempt.send_email()

        return Response(
            {
                'message': 'User registration success, please check your email to confirm your registration.',
                'status': 'success'
            },
            status=status.HTTP_201_CREATED
        )


class RegistrationConfirmationView(APIView):
    """
    Provides the ability to confirm an user registration
    """

    #@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    def post(self, request):
        request_serializer = EmailConfirmationSerializer(data=request.data)
        

        if not request_serializer.is_valid(raise_exception=True):
            return Response(
                {
                    'message': 'The confirmation link was invalid or used.',
                    'status': 'failed'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():
            attempt = RegistrationHandler.objects.filter(token=request_serializer.validated_data['token']).first()

            if attempt is None:
                return Response(
                    {
                        'message': 'The confirmation link was invalid or used.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if attempt.is_confirmed:
                return Response(
                    {
                        'message': 'The confirmation link was invalid or used.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not attempt.is_confirmed:
                attempt.user.is_confirmed = True
                attempt.user.save()
                attempt.is_confirmed = True
                attempt.save()

        return Response(
            {
                'message': 'Your email has been succesfully confirmed.',
                'status': 'success'
            },
            status=status.HTTP_202_ACCEPTED
        )


class ForgotPasswordHandlerView(APIView):
    """
    Provides the ability to obtain a reset password email.
    """

    ##@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    def post(self, request):
        request_serializer = PasswordResetRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        email = request_serializer.validated_data['email'].lower()

        os = request.user_agent.os.family + ' ' + request.user_agent.os.version_string
        browser = request.user_agent.browser.family

        with transaction.atomic():
            user = User.objects.filter(email=email).first()

            if user is not None:
                if hasattr(user, 'password_token'):
                    user.password_token.delete()
                attempt = ForgotPasswordHandler.objects.create(user=user, browser=browser, operating_system=os)
                attempt.send_email()

            return Response(
                    {
                        'message': 'Please check using your registered email to perform password reset.',
                        'status': 'success'
                    },
                    status=status.HTTP_200_OK
                )

class CheckConfirmPasswordTokenView(APIView):

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)

    def post(self, request):
        request_serializer = EmailConfirmationSerializer(data=request.data)

        if not request_serializer.is_valid():
            return Response(
                {
                    'message': 'The confirmation link was invalid.',
                    'status': 'failed'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():

            attempt = ForgotPasswordHandler.objects.filter(token=request_serializer.validated_data['token']).first()

            if attempt is None:
                return Response(
                    {
                        'message': 'The confirmation link was invalid or used.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if attempt.get_time_diff > 3600 * 24:
                return Response(
                    {
                        'message': 'The confirmation link was expired. Please obtain a new reset password request.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if attempt.is_confirmed:
                return Response(
                    {
                        'message': 'The confirmation link was invalid or used.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(
            {
                'message': 'Token valid and could be use to reset password.',
                'status': 'success'
            },
            status=status.HTTP_200_OK
        )


class ConfirmForgotPasswordHandlerView(APIView):
    """
    Provides the ability to reset password.
    """

    ##@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    # @method_decorator(sensitive_post_parameters('new_password'))
    @method_decorator(never_cache)
    def post(self, request):

        request_serializer = PasswordResetConfirmationRequestSerializerPost(
            data=request.data)
        request_serializer.is_valid(raise_exception=True)
        new_password = request_serializer.validated_data['new_password']
        token = request_serializer.validated_data['token']

        if not token:
            return Response(
                {
                    'message': 'The confirmation link was invalid or used.',
                    'status': 'failed'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():

            attempt = ForgotPasswordHandler.objects.filter(token=token).first()

            if attempt is None:
                return Response(
                    {
                        'message': 'The confirmation link was invalid or used.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if attempt.is_confirmed:
                return Response(
                    {
                        'message': 'The confirmation link was invalid or used.',
                        'status': 'failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not attempt.is_confirmed:
                attempt.user.is_confirmed = True
                attempt.user.set_password(new_password)
                attempt.user.save()
                attempt.is_confirmed = True
                attempt.save()

        return Response(
            {
                'message': 'Password has been changed.',
                'status': 'success'
            },
            status=status.HTTP_200_OK
        )


class ChangePasswordView(APIView):
    """
    Provides the ability to change password.
    """

    serializer_class = PasswordChangeRequestSerializer

    ##@method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)

    def post(self, request):

        if request.user.is_anonymous:
            return Response(
                {
                    'message': 'Please login to proceed.',
                    'status': 'failed'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        request_serializer = PasswordChangeRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        password = request_serializer.validated_data['password']
        new_password = request_serializer.validated_data['new_password']

        if not request.user.check_password(password):
            return Response(
                {
                    'message': 'Old password wrong.',
                    'status': 'failed'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.set_password(new_password)
        request.user.save()

        logout(request)

        return Response(
            {
                'message': 'Password has been changed.',
                'status': 'success'
            },
            status=status.HTTP_200_OK
        )

class UpdateProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)

    def post(self, request):
        if(not request.user):
            return Response(
                {
                    'message': 'Error No User Supplied',
                    'status': 'failed'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        request_serializer = UpdateProfileSerializer
        request_serializer.is_valid(raise_exception=True)

        id_line = request_serializer.validated_data['id_line']
        nomor_telepon = request_serializer.validated_data['nomor_telepon']
        is_vege = request_serializer.validated_data['is_vege']
        alergic = request_serializer.validated_data['alergic']

        with transaction.atomic():

            current_user = request.user
            u = User.objects.get(id=current_user.id)
            u.id_line = id_line
            u.nomor_telepon = nomor_telepon
            u.is_vege = is_vege
            u.alergic = alergic
            u.save(['id_line', 'nomor_telepon', 'is_vege', 'alergic'])

            return Response(
                {
                    'message': 'berhasil update profile',
                    'status': 'success'
                },
                status=status.HTTP_200_OK
            )


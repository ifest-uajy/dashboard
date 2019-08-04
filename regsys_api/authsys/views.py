"""
authsys views configurations
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db import transaction
from rest_framework.views import (APIView)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import status, permissions
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .models import (
    User,
    RegistrationHandler,
    ForgotPasswordHandler
)

from .serializers import (
    UserSerializer,
    LoginRequestSerializer,
    RegistrationRequestSerializer,
    RegistrationConfirmationRequestSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmationRequestSerializerPost,
    PasswordChangeRequestSerializer,
)


class GetUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response_serializer = UserSerializer(request.user)
        return Response(data=response_serializer.data)


@csrf_protect
@ensure_csrf_cookie
@sensitive_post_parameters('password')
@api_view(['POST'])
def login_view(request):
    """
    Fungsi login
    :: Parameter email
    :: Parameter password
    """
    request_serializer = LoginRequestSerializer(data=request.data)
    request_serializer.is_valid(raise_exception=True)

    user = authenticate(
        email=request_serializer.validated_data['email'].lower(),
        password=request_serializer.validated_data['password']
    )

    if user is None:
        return Response(
            {
                'status': 'failed',
                'message': 'Wrong email or password.'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not user.is_confirmed:
        return Response(
            {
                'status': 'failed',
                'message': 'Account email hasn\'t been confirmed.'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    user.last_login = timezone.now()
    user.save()

    login(request, user)
    response_serializer = UserSerializer(request.user)
    return Response(data=response_serializer.data)


@csrf_protect
@ensure_csrf_cookie
@permission_classes((permissions.IsAuthenticated))
@api_view(['POST'])
def _logout_view(request):
    """
    Fungsi logout
    """
    logout(request)
    return Response()


@csrf_protect
@ensure_csrf_cookie
@sensitive_post_parameters('password')
@api_view(['POST'])
def _register_user(request):
    """
    Fungsi registrasi
    :: Parameter nama lengkap
    :: Parameter email
    :: Parameter password
    """
    serial = RegistrationRequestSerializer(data=request.data)
    serial.is_valid(raise_exception=True)

    with transaction.atomic():
        user = User.objects.create_user(
            email=serial.validated_data['email'].lower(),
            password=serial.validated_data['password'],
            full_name=serial.validated_data['full_name']
        )

        auth_go = RegistrationHandler.objects.create(user=user)
        auth_go.send_email()

    return Response({
        'message': 'User has been registered, please check your email to confirm your registration.'
    }, status=status.HTTP_201_CREATED)


class RegistrationConfirmationView(APIView):
    def get(self, request):

        token = request.GET.get('token')

        if not token:
            return Response({
                'status': 'failed',
                'message': 'Invalid token.'
            }, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            attempt = RegistrationHandler.objects.filter(token=token).first()

            if attempt is None:
                return Response({
                    'status': 'failed',
                    'message': 'Invalid token.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if attempt.is_confirmed:
                return Response({
                    'status': 'failed',
                    'message': 'The token has been used before.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not attempt.is_confirmed:
                attempt.user.is_confirmed = True
                attempt.user.save()
                attempt.is_confirmed = True
                attempt.save()

        return Response({
            'status': 'success',
            'message': 'Your email has been succesfully confirmed.'
        })


class ForgotPasswordHandlerView(APIView):
    def post(self, request):

        request_serializer = PasswordResetRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        email = request_serializer.validated_data['email'].lower()

        with transaction.atomic():
            user = User.objects.filter(email=email).first()

            if user is not None:
                if hasattr(user, 'password_token'):
                    user.password_token.delete()
                attempt = ForgotPasswordHandler.objects.create(user=user)
                attempt.send_email()

        return Response({
            'status': 'success',
            'message': 'Please check using your registered email to perform password reset.'
        }, status=status.HTTP_200_OK)


class ResetPasswordHandler(APIView):
    def get(self, request):

        token = request.GET.get('token')

        if not token:
            return Response({
                'status': 'failed',
                'message': 'Invalid token.'
            }, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            attempt = ForgotPasswordHandler.objects.filter(token=token).first()

            if attempt is None:
                return Response({
                    'status': 'failed',
                    'message': 'Invalid token.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if attempt.is_confirmed:
                return Response({
                    'status': 'failed',
                    'message': 'The token has been used before.'
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'success',
            'message': 'Token valid.'
        })

    def post(self, request):

        request_serializer = PasswordResetConfirmationRequestSerializerPost(
            data=request.data)
        request_serializer.is_valid(raise_exception=True)
        new_password = request_serializer.validated_data['new_password']

        token = request.GET.get('token')

        if not token:
            return Response({
                'status': 'failed',
                'message': 'Invalid token.'
            }, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            attempt = ForgotPasswordHandler.objects.filter(token=token).first()

            if attempt is None:
                return Response({
                    'status': 'failed',
                    'message': 'Invalid token.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if attempt.is_confirmed:
                return Response({
                    'status': 'failed',
                    'message': 'The token has been used before.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not attempt.is_confirmed:
                attempt.user.is_confirmed = True
                attempt.user.set_password(new_password)
                attempt.user.save()
                attempt.is_confirmed = True
                attempt.save()

        return Response({
            'status': 'success',
            'message': 'Password has been changed.'
        })


class RegisterView(APIView):

    permission_classes = ()

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

        return Response({
            'message': 'registration success',
            'detail': 'Silahkan konfirmasi email anda'
        })

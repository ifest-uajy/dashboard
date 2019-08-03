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
    PasswordResetConfirmationRequestSerializer,
    PasswordChangeRequestSerializer,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone


class GetUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response_serializer = UserSerializer(request.user)
        return Response(data=response_serializer.data)


class LoginView(APIView):
    permission_classes = ()

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

        refresh = RefreshToken.for_user(user)

        user.last_login = timezone.now()
        user.save()

        return Response(
            {
                'status': 'success',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            },
            status=status.HTTP_200_OK
        )


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

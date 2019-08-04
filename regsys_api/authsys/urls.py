from django.urls import path
from .views import (
    GetUser, RegisterView, LoginView, RegistrationConfirmationView,
    ForgotPasswordHandlerView, ResetPasswordHandler
)

urlpatterns = [
    path('', GetUser.as_view(), name='get_details'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirm/', RegistrationConfirmationView.as_view(), name='confirm_email'),
    path('reset/confirm/', ResetPasswordHandler.as_view(),
         name='reset_password_token'),
    path('reset/', ForgotPasswordHandlerView.as_view(), name='reset_password'),
]

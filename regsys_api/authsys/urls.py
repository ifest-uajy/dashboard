"""
regsys_api.authsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    LoginView, RegistrationView, LogoutView,
    RegistrationConfirmationView,
    ForgotPasswordHandlerView, GetCurrentUserView,
    ConfirmForgotPasswordHandlerView, ChangePasswordView,
    CheckConfirmPasswordTokenView,
    UpdateProfileView, ResendActivationHandlerView)

urlpatterns = [
    path('', GetCurrentUserView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('confirm/', RegistrationConfirmationView.as_view()),
    path('reset/confirm/', ConfirmForgotPasswordHandlerView.as_view()),
    path('reset/check/', CheckConfirmPasswordTokenView.as_view()),
    path('reset/', ForgotPasswordHandlerView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('profile/update/', UpdateProfileView.as_view()),
    path('confirm/resend/', ResendActivationHandlerView.as_view())
]

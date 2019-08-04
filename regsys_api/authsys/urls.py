from django.urls import path
from .views import LoginView, RegistrationView, LogoutView, RegistrationConfirmationView, ForgotPasswordHandlerView, GetCurrentUserView, ConfirmForgotPasswordHandlerView, ChangePasswordView

urlpatterns = [
    path('', GetCurrentUserView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('confirm/', RegistrationConfirmationView.as_view()),
    path('reset/confirm/', ConfirmForgotPasswordHandlerView.as_view()),
    path('reset/', ForgotPasswordHandlerView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
]

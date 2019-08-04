from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import (
    GetUser, RegisterView, _register_user, login_view, _logout_view, RegistrationConfirmationView,
    ForgotPasswordHandlerView, ResetPasswordHandler
)

urlpatterns = [
    path('', GetUser.as_view(), name='get_details'),
    path('register/', _register_user),
    path('login/', login_view),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirm/', RegistrationConfirmationView.as_view(), name='confirm_email'),
    path('reset/confirm/', ResetPasswordHandler.as_view(),
         name='reset_password_token'),
    path('reset/', ForgotPasswordHandlerView.as_view(), name='reset_password'),
    path('logout/', _logout_view)
]

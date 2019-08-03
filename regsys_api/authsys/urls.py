from django.urls import path
from .views import GetUser, RegisterView, LoginView

urlpatterns = [
    path('', GetUser.as_view(), name='get_details'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
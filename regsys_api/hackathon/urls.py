from django.urls import path
from .views import (
    RegisterTeamView
)

urlpatterns = [
    path('register/', RegisterTeamView.as_view()),
]
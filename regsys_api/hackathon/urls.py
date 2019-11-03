from django.urls import path
from .views import (
    RegisterTeamView, ListTrackView, GetTeamUserView
)

urlpatterns = [
    path('register/', RegisterTeamView.as_view()),
    path('', ListTrackView.as_view()),
    path('teams/', GetTeamUserView.as_view())
]
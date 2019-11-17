from django.urls import path
from .views import (
    RegisterTeamView, ListTrackView, GetTeamUserView, JoinTeam, addTaskResponse
)

urlpatterns = [
    path('register/', RegisterTeamView.as_view()),
    path('', ListTrackView.as_view()),
    path('teams/', GetTeamUserView.as_view()),
    path('teams/join/', JoinTeam.as_view()),
    path('teams/task/add/', addTaskResponse.as_view()),
]
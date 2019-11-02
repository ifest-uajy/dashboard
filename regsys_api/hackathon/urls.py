from django.urls import path
from .views import (
    RegisterTeamView, ListTrackView
)

urlpatterns = [
    path('register/', RegisterTeamView.as_view()),
    path('', ListTrackView.as_view())
]
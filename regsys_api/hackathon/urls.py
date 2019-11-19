from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from .views import (
    RegisterTeamView, ListTrackView, GetTeamUserView, JoinTeam, addTaskResponse, ListHackathonTeams,  GetTeamById
)

urlpatterns = [
    path('register/', RegisterTeamView.as_view()),
    path('', ListTrackView.as_view()),
    path('teams/', GetTeamUserView.as_view()),
    path('teams/join/', JoinTeam.as_view()),
    path('teams/task/add/', addTaskResponse.as_view()),
    url('^admin/team/list/(?P<slug>.+)/$', permission_required('is_staff')(ListHackathonTeams.as_view()), name='team_list'),
    url('^admin/detail/(?P<id>.+)/$', permission_required('is_staff')(GetTeamById.as_view()), name='team_list'),
]
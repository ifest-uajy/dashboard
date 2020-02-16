from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from .views import (
    RegisterTeamView, ListTrackView, GetTeamUserView, JoinTeam, addTaskResponse, ListHackathonTeams,  GetTeamById,
    DetailTeam, AdminTaskHandler
)

urlpatterns = [
    path('register/', RegisterTeamView.as_view()),
    path('', ListTrackView.as_view()),
    path('teams/', GetTeamUserView.as_view()),
    path('teams/join/', JoinTeam.as_view()),
    path('admin/task/handler/', AdminTaskHandler.as_view()),
    path('teams/task/add/', addTaskResponse.as_view()),
    url('^admin/team/slug-detail/(?P<slug>.+)/$', DetailTeam.as_view(), name='team_list'),
    url('^admin/team/list/(?P<slug>.+)/$', ListHackathonTeams.as_view(), name='team_list'),
    url('^admin/detail/(?P<id>.+)/$', GetTeamById.as_view(), name='team_list'),
]

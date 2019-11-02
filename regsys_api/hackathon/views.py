from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status, generics, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from regsys_api.authsys.models import User
from .models import (
    Track,
    HackathonTeams,
    HackathonTeamsMember
)

from .serializers import (
    HackathonTeamsDetailSerializer,
    HackathonTeamsMemberSerializer,
    HackathonTeamsSerializer,
    TrackSerializer,
    RegisterHackathonTeamSerializer,
    AddHackathonTeamMemberSerializer
)

class ListTrackView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    #permission_classes = (IsAuthenticated,)

class RegisterTeamView(views.APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, **extra_fields):
        request_serializer = RegisterHackathonTeamSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        track = request_serializer.validated_data['track_id']
        team_name = request_serializer.validated_data['name']
        team_institution = request_serializer.validated_data['institution']

        with transaction.atomic():

            if HackathonTeamsMember.objects.filter(team__track=track, user=request.user).exists():
                return Response(
                    {
                        'message': 'This competition has been registered with this user',
                        'status': 'failed',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            new_team = HackathonTeams.objects.create(
                track=track,
                name=team_name,
                institution=team_institution,
                team_leader=request.user
            )

            HackathonTeamsMember.objects.create(
                team=new_team,
                user=request.user
            )

            response_serializer = HackathonTeamsSerializer(new_team)
            print(response_serializer)
            return Response(data=response_serializer.data)

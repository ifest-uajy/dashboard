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
    permission_classes = (IsAuthenticated,)

class RegisterTeamView(views.APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, **extra_fields):
        request_serializer = RegisterHackathonTeamSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        slug = request_serializer.validated_data['slug_name']
        track = Track.objects.filter(slug_name=slug).first()

        name = request_serializer.validated_data['name']
        team_institution = request_serializer.validated_data['team_institution']

        alamat_institution = request_serializer.validated_data['alamat_institution']
        nama_pembimbing  = request_serializer.validated_data['nama_pembimbing']
        no_telp_pembimbing = request_serializer.validated_data['no_telp_pembimbing']

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
                name=name,
                institution=team_institution,
                team_leader=request.user,
                alamat_institusi=alamat_institution,
                nama_pendamping=nama_pembimbing,
                nomor_telepon_pendamping=no_telp_pembimbing
            )

            HackathonTeamsMember.objects.create(
                team=new_team,
                user=request.user
            )

            return Response(
                    {
                        'message': 'Tim anda sudah terdaftar.',
                        'status': 'success',
                    },
                    status=status.HTTP_201_CREATED
                )

class GetTeamUserView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HackathonTeamsDetailSerializer

    def get_queryset(self):
        return HackathonTeams.objects.filter(team_members__user=self.request.user)

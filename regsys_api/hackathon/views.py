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
    AddHackathonTeamMemberSerializer,
    JoinTeamSerializer
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


class JoinTeam(views.APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, **extra_fields):
        request_serializer = JoinTeamSerializer(data=request.data)

        request_serializer.is_valid(raise_exception=True)

        token = request_serializer.validated_data['token']

        team = HackathonTeams.objects.filter(
            invitation_token=token
        ).first()

        if not team:
            return Response(
                    {
                        'message': 'Tim tidak di temukan.',
                        'status': 'failed',
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        if HackathonTeamsMember.objects.filter(team__track=team.track, user=request.user).exists():
                return Response(
                    {
                        'message': 'Anda telah bergabung dalam kompetisi ini.',
                        'status': 'failed',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                    
                )

        if team.jumlah_member == team.track.team_max_member:
            return Response(
                {
                    'message': 'Maaf tim ini sudah penuh',
                    'status': 'failed'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        HackathonTeamsMember.objects.create(
                team=team,
                user=request.user
            )

        return Response(
                    {
                        'message': 'Anda sudah terdaftar.',
                        'status': 'success',
                    },
                    status=status.HTTP_201_CREATED
                )
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status, generics, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from regsys_api.authsys.models import User
import requests
from threading import Thread
import json
from .models import (
    Track,
    HackathonTeams,
    HackathonTeamsMember,
    HackathonTask,
    TaskResponse
)

from .serializers import (
    HackathonTeamsDetailSerializer,
    AdminTeamDetailSerializer,
    HackathonTeamsMemberSerializer,
    HackathonTeamsSerializer,
    TeamDetailSerializer,
    TrackSerializer,
    RegisterHackathonTeamSerializer,
    AddHackathonTeamMemberSerializer,
    JoinTeamSerializer,
    PostTaskResponseSerializer,
    TaskResponseSerializer,
    AdminConfirmTask,
    TeamMemberSerializer
)
from django.utils import timezone


class ListTrackView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (IsAuthenticated,)


class ListHackathonTeams(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = HackathonTeamsSerializer

    def get_queryset(self):
        return HackathonTeams.objects.filter(track__slug_name=self.kwargs['slug'])


class RegisterTeamView(views.APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, **extra_fields):
        request_serializer = RegisterHackathonTeamSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=request.user.email).first()

        if user.isProfileComplete is False:
            return Response(
                    {
                        'message': 'Profil anda belum lengkap untuk membuat tim.',
                        'status': 'failed',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

        slug = request_serializer.validated_data['slug_name']
        track = Track.objects.filter(slug_name=slug).first()

        name = request_serializer.validated_data['name']
        team_institution = request_serializer.validated_data['team_institution']

        alamat_institution = request_serializer.validated_data['alamat_institution']
        nama_pembimbing = request_serializer.validated_data['nama_pembimbing']
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

            Thread(target=new_team.send_line_notification).start()
            Thread(target=new_team.send_email).start()

            return Response(
                    {
                        'message': 'Tim anda sudah terdaftar.',
                        'status': 'success',
                    },
                    status=status.HTTP_201_CREATED
                )


class GetTeamUserView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamDetailSerializer

    def get_queryset(self):
        return HackathonTeams.objects.filter(team_members__user=self.request.user)


class JoinTeam(views.APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, **extra_fields):
        request_serializer = JoinTeamSerializer(data=request.data)

        request_serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=request.user.email).first()

        if user.isProfileComplete is False:
            return Response(
                    {
                        'message': 'Profil anda belum lengkap untuk bergabung kedalam tim.',
                        'status': 'failed',
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

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


class addTaskResponse(views.APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):

        request_serializer = PostTaskResponseSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        team = get_object_or_404(
            HackathonTeams.objects.all(),
            id=request_serializer.validated_data['team_id'],
            team_members__user=self.request.user
        )

        task = get_object_or_404(
            HackathonTask.objects.all(),
            id=request_serializer.validated_data['task_id'],
        )

        if timezone.now() > task.deadline:
            return Response(
                {
                    'message': 'Sudah deadline',
                    'status': 'failed'
                }, status=status.HTTP_403_FORBIDDEN
            )

        response = request_serializer.validated_data['response']

        if team.bisa_up_task and not team.is_blacklisted and team.current_task.pk is task.pk:

            if task.require_validation:
                task_response_status = TaskResponse.WAITING
                task_done = False
            else:
                task_response_status = TaskResponse.DONE
                task_done = True
                team.move_one_step()

            new_response = TaskResponse.objects.update_or_create(
                task=task,
                team=team,
                defaults={
                    'response': response,
                    'status': task_response_status,
                    'updated_at': timezone.now(),
                    'is_verified': task_done,
                }
            )

            if task.task_type == HackathonTask.PAYMENT_SUBMISSION:
                Thread(target=new_response[0].send_email_p).start()

            Thread(target=new_response[0].send_line_notification).start()

            response_serializer = TaskResponseSerializer(new_response[0])

            return Response(
                data=response_serializer.data, status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                {
                    'message': 'Error task lomba tidak berhasil dibuat.',
                    'status': 'failed'
                }, status=status.HTTP_403_FORBIDDEN
            )


class GetTeamById(views.APIView):
    permission_classes = (IsAuthenticated, IsAdminUser, )

    def get(self, request, **kwargs):

        user = User.objects.filter(email=request.user.email).first()

        if user.is_staff is False:
            return Response(
                {
                    'message': 'Error route for staff.',
                    'status': 'failed'
                }, status=status.HTTP_403_FORBIDDEN
            )

        team = get_object_or_404(
            HackathonTeams.objects.all(),
            id=self.kwargs['id']
        )

        response_serializer = AdminTeamDetailSerializer(team)

        return Response(
            data=response_serializer.data, status=status.HTTP_200_OK
        )


class DetailTeam(views.APIView):
    permission_classes = (IsAuthenticated, IsAdminUser, )

    def get(self, request, **kwargs):

        track = Track.objects.filter(slug_name=self.kwargs['slug'])

        response_serializer = TrackSerializer(track[0])

        return Response(
            data=response_serializer.data, status=status.HTTP_200_OK
        )

class TeamMemberHandler(views.APIView):
    """
        Handler untuk POST dan GET team member.
        Kelas ini berfungsi untuk menambah, mengedit dan menampilkan
        data anggota kelompok selain ketua.
    """

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        """
            Fungsi untuk menambahkan anggota tim kedalam tim oleh ketua tim
        """

        req_serializer = TeamMemberSerializer(data=request.data)
        req_serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=request.user.email).first()

        #TODO buat masukin user ke team ganti semua team member yg lama


class AdminTaskHandler(views.APIView):
    permission_classes = (IsAuthenticated, IsAdminUser, )

    def post(self, request):

        request_serializer = AdminConfirmTask(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        task_id = request_serializer.validated_data['task_res_id']

        task = get_object_or_404(TaskResponse, pk=task_id)

        if task:

            if request.user.groups.filter(name='Pengurus Harian').exists() or request.user.groups.filter(name='Sekretariat').exists():

                if task.status == TaskResponse.DONE:
                    return Response(
                        {
                            'message': 'Tidak ada yang perlu diverifikasi.',
                            'status': 'success'
                        }, status=status.HTTP_200_OK
                    )

                if not request_serializer.validated_data['tolak']:
                    task.is_verified = True

                    task.status = TaskResponse.DONE

                    if task.task.task_type == HackathonTask.PAYMENT_SUBMISSION:
                        if request.user.groups.filter(name='Pengurus Harian').exists():
                            Thread(
                                target=task.send_email_pembayaran_selesai).start()
                        else:
                            return Response(
                                {
                                    'message': 'PH tok yang boleh',
                                    'status': 'failed'
                                }, status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        if not request.user.groups.filter(name='Sekretariat').exists():
                            return Response(
                                {
                                    'message': 'Hanya sekret yang bisa boi.',
                                    'status': 'failed'
                                }, status=status.HTTP_400_BAD_REQUEST
                            )

                    task.save()
                    task.team.move_one_step()

                else:

                    if task.task.task_type == HackathonTask.PAYMENT_SUBMISSION:
                        if not request.user.groups.filter(name='Pengurus Harian').exists():
                            return Response(
                                {
                                    'message': 'PH tok yang boleh',
                                    'status': 'failed'
                                }, status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        if not request.user.groups.filter(name='Sekretariat').exists():
                            return Response(
                                {
                                    'message': 'Hanya sekret yang bisa boi.',
                                    'status': 'failed'
                                }, status=status.HTTP_400_BAD_REQUEST
                            )

                    task.is_verified = False

                    task.status = TaskResponse.REJECTED
                    Thread(target=task.send_email_tolak).start()
                    task.save()

                return Response(
                    {
                        'message': 'Respon tugas berhasil diverifikasi.',
                        'status': 'success'
                    }, status=status.HTTP_202_ACCEPTED
                )

            else:
                return Response(
                    {
                        'message': 'Anda tidak memiliki permission untuk melakukan ini',
                        'status': 'failed'
                    }, status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {
                    'message': 'Respon tugas tidak ditemukan.',
                    'status': 'failed'
                }, status=status.HTTP_404_NOT_FOUND
            )

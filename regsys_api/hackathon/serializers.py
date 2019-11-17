from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from regsys_api.authsys.models import User
from .models import Track, HackathonTeams, HackathonTeamsMember, HackathonTask, TaskResponse
from regsys_api.authsys.serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
import json


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = (
            'id', 'name', 'team_min_member', 'team_max_member', 'description', 'closed_date', 'name', 'isExpired', 'slug_name', 'biaya_pendaftaran'
        )



class HackathonTeamsMemberSerializer(serializers.ModelSerializer):

    nama = serializers.ReadOnlyField(
        source="user.full_name",
        read_only=True
    )

    class Meta:
        model = HackathonTeamsMember
        fields = ('nama', )

class HackathonTeamsSerializer(serializers.ModelSerializer):

    track = TrackSerializer(read_only=True)
    team_leader_name = serializers.SlugRelatedField(
        source='team_leader',
        slug_field='full_name',
        read_only=True,
    )

    class Meta:
        model = HackathonTeams
        fields = (
            'id', 'name', 'track', 'team_leader_name', 'institution', 'is_blacklisted'
        )
        read_only_fields = (
            'id', 'track', 'team_leader_name', 'institution', 'is_blacklisted'
        
        )

class TaskResponseSerializer(serializers.ModelSerializer):
    
    #task_id = HackathonTaskSerializer(source='team')
    #task = HackathonTaskSerializer(read_only=True)

    class Meta:
        model = TaskResponse
        fields = ('task_id', 'response', 'status', 'updated_at', 'is_verified')
        read_only_fields = ('task_id', )

class HackathonTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackathonTask
        fields = (
            'id', 'name', 'deadline', 'deskripsi', 'order', 'task_type'
        )

class HackathonTeamsDetailSerializer(serializers.ModelSerializer):

    track = TrackSerializer(read_only=True)
    team_leader_name = serializers.SlugRelatedField(
        source='team_leader', slug_field='full_name', queryset=User.objects.all()
    )
    team_members = HackathonTeamsMemberSerializer(many=True, read_only=True)

    current_task = HackathonTaskSerializer(read_only=True)

    task_list = HackathonTaskSerializer(many=True)

    task_response_list = TaskResponseSerializer(many=True, read_only=True)

    class Meta:
        model = HackathonTeams
        fields = (
            'task_list', 'id', 'task_response_list', 'track', 'name', 'team_leader_name', 'institution', 'is_blacklisted', 'team_members', 'created_at', 'invitation_token', 'current_task', 'bisa_up_task'
        )
        read_only_fields = (
            'task_list', 'id', 'task_response_list', 'track', 'name', 'team_leader_name', 'institution', 'is_blacklisted', 'team_members', 'created_at', 'invitation_token', 'current_task', 'bisa_up_task'
        )

class RegisterHackathonTeamSerializer(serializers.Serializer):
    slug_name = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100, min_length=3, validators=[UniqueValidator(queryset=HackathonTeams.objects.all())])
    team_institution = serializers.CharField(max_length=50)
    alamat_institution = serializers.CharField(max_length=500)
    nama_pembimbing = serializers.CharField(max_length=50)
    no_telp_pembimbing = serializers.CharField(max_length=20)

class AddHackathonTeamMemberSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

class JoinTeamSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=50)

class TeamDetailSerializer(serializers.ModelSerializer):

    kompetisi = TrackSerializer(source='track', read_only=True)

    nama = serializers.CharField(source='name', read_only=True)
    asal = serializers.CharField(source='institution', read_only=True)
    alamat = serializers.CharField(source='alamat_institusi')

    ketua = serializers.SlugRelatedField(
        source='team_leader', slug_field='full_name', queryset=User.objects.all()
    )
    pembimbing = serializers.SerializerMethodField('get_info_pembimbing')
    #anggota = HackathonTeamsMemberSerializer(source='team_members', many=True)
    anggota = serializers.SerializerMethodField('get_info_anggota')
    
    token = serializers.CharField(source='invitation_token', read_only=True)
    ditangguhkan = serializers.BooleanField(source='is_blacklisted', read_only=True)

    tasks = serializers.SerializerMethodField('get_info_task')

    #response = TaskResponseSerializer(source='task_response', many=True, read_only=True)
    
    current_task = HackathonTaskSerializer(read_only=True)

    task_permission = serializers.BooleanField(source='bisa_up_task')

    #task_list = HackathonTaskSerializer(many=True)

    class Meta:
        model = HackathonTeams
        fields = (
            'id',
            'kompetisi', 'nama', 'asal', 'alamat', 'ketua', 'pembimbing', 'anggota',
            'token', 'ditangguhkan', 'created_at', 'tasks', 'current_task', 'task_permission' # 'tasks'
        )

    #def get_info_task(self, obj):
    #    tasks = TaskResponse.objects.filter(team=obj).all()
    #    return HackathonTaskSerializer(tasks, many=True)

    def get_info_pembimbing(self, obj):
        return {
            'nama': obj.nama_pendamping,
            'telepon': obj.nomor_telepon_pendamping
        }

    def get_info_anggota(self, obj):
        queryset = HackathonTeamsMember.objects.filter(team=obj).values('user').distinct()
        return json.loads(
            json.dumps(list(queryset.values_list('user__full_name', flat=True)))
        )

    def get_info_task(self, obj):
        data = []
        queryset = HackathonTask.objects.filter(track=obj.track)

        list_qs = list(queryset.values())

        json_list_all = json.loads("[]")

        for e in queryset:

            json_list = json.loads(
            '{"task" : [], "response": []}'
            )

            qs_response = TaskResponse.objects.filter(team=obj, task=e).first()

            if qs_response:

                json_list["task"] = json.loads(
                        json.dumps(HackathonTaskSerializer(e).data)
                    )
                
                
                json_list["response"] = json.loads(
                        json.dumps(TaskResponseSerializer(qs_response).data)
                    )

            else:
                json_list["task"] = json.loads(
                        json.dumps(HackathonTaskSerializer(e).data)
                    )
                

            json_list_all.append(json_list)

        return json_list_all
"""
    def get_info_task(self, obj):
        queryset = HackathonTask.objects.filter(track=obj.track)
        return json.loads(
            json.dumps(list(HackathonTaskSerializer(queryset, many=True).data))
        )
        """

class PostTaskResponseSerializer(serializers.Serializer):
    team_id = serializers.CharField(max_length=10)
    task_id = serializers.CharField(max_length=10)
    response = serializers.CharField(max_length=500)
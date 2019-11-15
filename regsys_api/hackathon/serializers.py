from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from regsys_api.authsys.models import User
from .models import Track, HackathonTeams, HackathonTeamsMember, HackathonTask, TaskResponse
from regsys_api.authsys.serializers import UserSerializer

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = (
            'id', 'name', 'team_min_member', 'team_max_member', 'description', 'closed_date', 'name', 'isExpired', 'slug_name', 'biaya_pendaftaran'
        )

class HackathonTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HackathonTask
        fields = (
            'name', 'deadline', 'order', 'task_type'
        )

class HackathonTeamsMemberSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(
        source="user.full_name",
        read_only=True
    )

    class Meta:
        model = HackathonTeamsMember
        fields = (
            'id', 'user'
        )
        read_only_fields = (
            'id', 'user'
        )

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
    
class HackathonTeamsDetailSerializer(serializers.ModelSerializer):

    track = TrackSerializer(read_only=True)
    team_leader_name = serializers.SlugRelatedField(
        source='team_leader', slug_field='full_name', queryset=User.objects.all()
    )
    team_members = HackathonTeamsMemberSerializer(many=True, read_only=True)

    current_task = HackathonTaskSerializer(read_only=True)

    task_list = HackathonTaskSerializer(many=True)

    class Meta:
        model = HackathonTeams
        fields = (
            'task_list', 'id', 'track', 'name', 'team_leader_name', 'institution', 'is_blacklisted', 'team_members', 'created_at', 'invitation_token', 'current_task', 'bisa_up_task'
        )
        read_only_fields = (
            'task_list', 'id', 'track', 'name', 'team_leader_name', 'institution', 'is_blacklisted', 'team_members', 'created_at', 'invitation_token', 'current_task', 'bisa_up_task'
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
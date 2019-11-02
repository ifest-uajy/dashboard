from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from regsys_api.authsys.models import User
from .models import Track, HackathonTeams, HackathonTeamsMember

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = (
            'id', 'name', 'team_min_member', 'team_max_member', 'description', 'closed_date', 'name', 'isExpired'
        )


class HackathonTeamsMemberSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(read_only=True)

    class Meta:
        model = HackathonTeamsMember
        fields = (
            'id', 'full_name', 'email'
        )
        read_only_fields = (
            'id', 'full_name', 'email'
        )

class HackathonTeamsSerializer(serializers.ModelSerializer):

    track = TrackSerializer(read_only=True)
    team_leader_email = serializers.SlugRelatedField(
        source='team_leader',
        slug_field='email',
        read_only=True,
    )

    class Meta:
        model = HackathonTeams
        fields = (
            'id', 'name', 'track', 'team_leader_email', 'institution', 'is_blacklisted'
        )
        read_only_fields = (
            'id', 'track', 'team_leader_email', 'institution', 'is_blacklisted'
        )
    
class HackathonTeamsDetailSerializer(serializers.ModelSerializer):

    track = TrackSerializer(read_only=True)
    team_leader_email = serializers.SlugRelatedField(
        source='team_leader', slug_field='email', queryset=User.objects.all()
    )
    team_members = HackathonTeamsMemberSerializer(many=True, read_only=True)

    class Meta:
        model = HackathonTeams
        fields = (
            'id', 'track', 'name', 'team_leader_email', 'institution', 'is_blacklisted', 'team_members', 'created_at'
        )
        read_only_fields = (
            'id', 'track', 'name', 'team_leader_email', 'institution', 'is_blacklisted', 'team_members', 'created_at'
        )

class RegisterHackathonTeamSerializer(serializers.Serializer):
    track_id = serializers.PrimaryKeyRelatedField(queryset=Track.objects.all())
    name = serializers.CharField(max_length=100, min_length=3, validators=[UniqueValidator(queryset=HackathonTeams.objects.all())])
    institution = serializers.CharField(max_length=50)

class AddHackathonTeamMemberSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
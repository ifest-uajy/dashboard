from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from regsys_api.authsys.models import User
from .models import Announcement

class AnnouncementSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    issued_at = serializers.DateTimeField()
    issuer = serializers.SlugRelatedField(
        slug_field='full_name',
        read_only = True
    )
    type = serializers.CharField(source='get_type_display')
    title = serializers.CharField(max_length=50)
    message = serializers.CharField()
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=75)
    email = serializers.EmailField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_confirmed = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            'full_name', 'email',
            'is_staff', 'is_confirmed', 'last_login', 'date_joined', 'isProfileComplete',
            'is_vege', 'alergic', 'is_buktiUploaded', 'id_line', 'nomor_telepon'
        )
        read_only_fields = (
            'email', 'is_staff', 'is_confirmed', 'last_login', 'date_joined',
        )


class LoginRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegistrationRequestSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=75)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField()

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmationRequestSerializerPost(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField()


class PasswordChangeRequestSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()

class EmailConfirmationSerializer(serializers.Serializer):
    token = serializers.CharField()

class UpdateProfileSerializer(serializers.Serializer):
    id_line = serializers.CharField()
    nomor_telepon = serializers.CharField()
    is_vege = serializers.BooleanField()
    alergic = serializers.CharField()
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class MessageSerializer(serializers.Serializer):

    nama_pengirim = serializers.CharField(max_length=50)
    email_pengirim = serializers.CharField(max_length=50)
    pesan = serializers.CharField(max_length=500)
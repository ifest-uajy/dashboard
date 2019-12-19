from rest_framework.response import Response
from django.db import transaction
from rest_framework.views import APIView
from rest_framework import status
from .models import Message
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .serializers import MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from threading import Thread

class MessageView(APIView):
    
    def post(self, request, **extra_fields):
        request_serializer = MessageSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        nama_pengirim = request_serializer.validated_data['nama_pengirim']
        email_pengirim = request_serializer.validated_data['email_pengirim']
        pesan = request_serializer.validated_data['pesan']

        with transaction.atomic():

            new_pesan = Message.objects.create(
                nama_pengirim = nama_pengirim,
                email_pengirim = email_pengirim,
                pesan = pesan
            )
            
            Thread(target=new_pesan.send_line_notification).start()
            Thread(target=new_pesan.send_email).start()
            

            return Response(
                {
                    'message': 'Pesan anda sudah dikirim',
                    'status': 'success'
                },
                status=status.HTTP_200_OK
            )

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.parsers import FileUploadParser
from .models import PersonalUploadFile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import uuid
from .models import PersonalUploadFile
from regsys_api.authsys.models import User
# Create your views here.
class PersonalUploadFileView(APIView):
    parser_clases = (FileUploadParser,)

    def put(self, request, format=None):
        file_obj = request.FILES['filename']
        
        if(file_obj):
            instance = PersonalUploadFile(
                id = uuid.uuid4(),
                original_filename = file_obj.name,
                file_size = file_obj.size,
                content_type = file_obj.content_type,
                uploaded_by = request.user,
            )
            instance.file = file_obj
            instance.save()

            return Response(
                {
                    'message': 'File anda berhasil di upload, terimakasih.',
                    'status': 'success',
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'File anda tidak berhasil di upload, terimakasih.',
                    'status': 'failed',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class getDownloadView(APIView):
    def get(self, request, **kwargs):
        fileID = self.kwargs['file_id']
        #queryset = PersonalUploadFile.objects.filter(uploaded_by=request.user)
        uploaded_file = get_object_or_404(PersonalUploadFile, id=fileID)
        #filename_baru = str(uuid.uuid1()) + ' ' + uploaded_file.original_filename
        response = HttpResponse(uploaded_file.file.open('rb'), content_type=uploaded_file.content_type)
        #response['Content-Disposition'] = 'inline; filename=' + uploaded_file.original_filename
        if not request.user:
            return Response(
                {
                    'message': 'Anda tidak memiliki ijin untuk mengunduh file ini. Pastikan ada memiliki kredensial yang tepat.',
                    'status': 'failed',
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        return response
        
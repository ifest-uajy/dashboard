from django.db import models

from regsys_api.authsys.models import User

class Message(models.Model):
    nama_pengirim = models.CharField(max_length=50)
    email_pengirim = models.CharField(max_length=50)
    pesan = models.CharField(max_length=500)
    recieved_at = models.DateTimeField(auto_now_add=True)



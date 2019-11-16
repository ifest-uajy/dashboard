from django.db import models

from regsys_api.authsys.models import User

class Message(models.Model):
    nama_pengirim = models.CharField(max_length=50)
    email_pengirim = models.CharField(max_length=50)
    pesan = models.TextField(max_length=500)
    recieved_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.nama_pengirim, self.email_pengirim)



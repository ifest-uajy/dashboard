from django.db import models

from regsys_api.authsys.models import User
from regsys_api.hackathon.models import HackathonTeams
import django.conf.global_settings as sett


def generate_upload_path(instance, filename):
    if instance.id is None:
        raise RuntimeError('Uploaded file ID has not been set.')
    return sett.MEDIA_ROOT + str(instance.id)


class PersonalUploadFile(models.Model):
    file = models.FileField(upload_to=generate_upload_path)
    id = models.UUIDField(primary_key=True, editable=False)
    original_filename = models.CharField(max_length=200)
    file_size = models.BigIntegerField()
    content_type = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(
        to=User, related_name='personal_uploaded_files', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename


class TeamUploadFile(models.Model):
    file = models.FileField(upload_to=generate_upload_path)
    id = models.UUIDField(primary_key=True, editable=False)
    original_filename = models.CharField(max_length=200)
    file_size = models.BigIntegerField()
    content_type = models.CharField(max_length=200)
    team_owner = models.ForeignKey(
        to=HackathonTeams, related_name='team_owner', on_delete=models.PROTECT)
    uploaded_by = models.ForeignKey(
        to=User, related_name='team_uploaded_files', on_delete=models.PROTECT)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename

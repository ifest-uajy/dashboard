from django.db import models

from regsys_api.authsys.models import User


class Thread(models.Model):
    thread_starter = models.ForeignKey(to=User, related_name='users', on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    started_at = models.DateTimeField(auto_now_add=True)

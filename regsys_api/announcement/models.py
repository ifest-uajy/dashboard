from django.db import models

from regsys_api.authsys.models import User

TYPE = (
    (1, 'info'),
    (2, 'error'),
    (3, 'success'),
    (4, 'warning'),
)


class Announcement(models.Model):
    issuer = models.ForeignKey(to=User, on_delete=models.PROTECT)
    type = models.IntegerField(choices=TYPE)
    issued_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    isShown = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def get_name(self):
        return issuer.full_name


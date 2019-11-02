from django.db import models
from django.utils.timezone import utc
import datetime

from regsys_api.authsys.models import User

class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    closed_date = models.DateTimeField(null=True)
    team_max_member = models.IntegerField(default=1)
    team_min_member = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    @property
    def isExpired(self):
        if self.closed_date:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            if(now > self.closed_date):
                return True
            else:
                return False

    class Meta:
        verbose_name = 'Competition Track'
        verbose_name_plural = 'Competition Tracks'

class HackathonTeams(models.Model):

    track = models.ForeignKey(
        to=Track, related_name='teams', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    institution = models.CharField(max_length=100)
    members = models.ManyToManyField(
        to=User, related_name='teams', through='HackathonTeamsMember')
    team_leader = models.ForeignKey(to=User, related_name='team_leader', on_delete=models.PROTECT)
    is_blacklisted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hackathon Team'
        verbose_name_plural = 'Hackathon Teams'
    
class HackathonTeamsMember(models.Model):

    team = models.ForeignKey(to=HackathonTeams, related_name='team_members', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='team_member', null=True, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.team.name, self.user.full_name, self.user.email)
    
    class Meta:
        unique_together = (('team', 'user'),)
        get_latest_by = 'created_at'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
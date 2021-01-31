from django.db.models import Q
from django.db import models
from django.utils.timezone import utc
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from xkcdpass import xkcd_password as xp
from django.core.mail import EmailMultiAlternatives
import json
from string import (
    ascii_letters, digits
)

from threading import Thread

from regsys_api.authsys.models import User
import requests
from django.template.loader import get_template
import sys
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _


def generate_token():
    return get_random_string(length=32, allowed_chars=ascii_letters + digits)


def getxkcdpass():
    wordfile = xp.locate_wordfile()
    config = xp.generate_wordlist(
        wordfile=wordfile, min_length=5, max_length=8)
    return (xp.generate_xkcdpassword(config, acrostic=False, delimiter="-", numwords=4))


class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # open_date = models.DateTimeField(null=True)
    closed_date = models.DateTimeField(null=True)
    team_max_member = models.IntegerField(default=1)
    team_min_member = models.IntegerField(default=1)
    slug_name = models.CharField(max_length=50)
    biaya_pendaftaran = models.IntegerField()
    is_shown = models.BooleanField()
    is_closed = models.BooleanField()
    slug_image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    @property
    def isExpired(self):
        if self.closed_date:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            if (now > self.closed_date):
                return True
            else:
                return False

    class Meta:
        verbose_name = 'Kompetisi'
        verbose_name_plural = 'Kompetisi'


class HackathonTask(models.Model):
    FILE_SUBMISSION = 'file_uploader'
    PAYMENT_SUBMISSION = 'payment_verification'
    ANNOUNCEMENT = 'pengumuman'
    TYPE_CHOICES = (
        (FILE_SUBMISSION, 'File Uploader'),
        (PAYMENT_SUBMISSION, 'Verifikasi Pembayaran'),
        (ANNOUNCEMENT, 'Pengumuman')
    )

    order = models.IntegerField()
    track = models.ForeignKey(
        to=Track, related_name='tracks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deskripsi = models.TextField()
    deadline = models.DateTimeField(null=True)
    task_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    require_validation = models.BooleanField(default=False)
    max_file_upload = models.IntegerField(default=10)

    def __str__(self):
        return "{} - {}".format(self.track, self.name)

    class Meta:
        verbose_name = 'Task Lomba'
        verbose_name_plural = 'Task Lomba'


class HackathonTeams(models.Model):
    track = models.ForeignKey(
        to=Track, related_name='teams', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)
    institution = models.CharField(max_length=100)
    alamat_institusi = models.CharField(max_length=500)
    """
    Field kontak pendamping
    """

    nama_pendamping = models.CharField(max_length=50)
    nomor_telepon_pendamping = models.CharField(max_length=20)

    """
    token
    """

    invitation_token = models.CharField(
        max_length=100, default=generate_token, unique=True)

    current_task = models.ForeignKey(
        to=HackathonTask, related_name='active', on_delete=models.PROTECT)

    members = models.ManyToManyField(
        to=User, related_name='teams', through='HackathonTeamsMember')
    team_leader = models.ForeignKey(
        to=User, related_name='team_leader', on_delete=models.PROTECT)
    is_blacklisted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def sudah_selesai_current_task(self):
        current_task_count = self.current_task
        update_current_task_count = self.task_response.filter(
            task=self.current_task, status=TaskResponse.DONE)
        return current_task_count == update_current_task_count

    @property
    def task_list(self):
        return HackathonTask.objects.filter(track=self.track).all()

    @property
    def task_response_list(self):
        return TaskResponse.objects.filter(team=self).all()

    @property
    def jumlah_member(self):
        return HackathonTeamsMember.objects.filter(team=self.pk).count()

    @property
    def bisa_up_task(self):
        if HackathonTeamsMember.objects.filter(team=self.pk).count() >= self.track.team_min_member:
            return True
        else:
            return False

    def move_one_step(self):

        if self.current_task.order + 1 <= HackathonTask.objects.filter(track=self.track).count():
            self.current_task = HackathonTask.objects.filter(
                Q(track=self.track), Q(order=self.current_task.order + 1)).first()
            self.save()

    def save(self, *args, **kwargs):
        if self.pk is None and not hasattr(self, 'current_task'):
            self.current_task = HackathonTask.objects.filter(
                track=self.track).first()

        super(HackathonTeams, self).save(*args, **kwargs)

    def send_line_notification(self):
        auth_token = 'JrtU8tFBrOugQLboQvaFpJdjlM5EvRIwUWaIwNwhGD5N6q1KcaouIgKd20VsJnNlQxc0RcBEf8nahzX6vJw9e51VcWA6BcQV+/F1PHNb5KVOGWxvvhM5CVyAx52RqInxmQGWQe8AToPTXLte/QUhUQdB04t89/1O/w1cDnyilFU='
        hed = {'Authorization': 'Bearer ' + auth_token}
        data = {
            "to": "C0fd8ac3ed9f41fe84d3de2d7581d52ed",
            "messages": [
                {
                    "type": "text",
                    "text": "[INFO TIM]\n{} ({}) baru saja mendaftar kompetisi {}.".format(self.name, self.institution,
                                                                                           self.track.name)
                }
            ]
        }

        url = 'https://api.line.me/v2/bot/message/push'

        requests.post(url, json=data, headers=hed)

    def send_email(self):
        context = {
            'nama_tim': self.name,
            'nama_kompetisi': self.track.name,
            'token': self.invitation_token,
            'harga': '{:20,.2f}'.format(self.track.biaya_pendaftaran),
            'title': 'Pendaftaran {} - IFest #8'.format(self.track.name)
        }

        text_template = get_template('selamat_datang.html')
        html_template = get_template('selamat_datang.html')
        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)
        mail = EmailMultiAlternatives(
            subject='Pendaftaran {} - IFest #8'.format(self.track.name),
            body=mail_text_message,
            to=[self.team_leader.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

    class Meta:
        verbose_name = 'Tim'
        verbose_name_plural = 'Tim'


class HackathonTeamsMember(models.Model):
    team = models.ForeignKey(
        to=HackathonTeams, related_name='team_members', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='team_member',
                             null=True, blank=True, on_delete=models.PROTECT)

    # Attribut umum user
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    nomor_id = models.CharField(max_length=50, blank=True)
    tanggal_lahir = models.DateField(default=None, null=True, blank=True)
    alamat = models.CharField(max_length=250, blank=True)

    # Attribut kontak user
    id_line = models.CharField(max_length=30, blank=True)
    nomor_telepon = models.CharField(max_length=13, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.team.name, self.full_name, self.email)

    class Meta:
        unique_together = (('team', 'user'),)
        get_latest_by = 'created_at'
        verbose_name = 'Anggota Tim'
        verbose_name_plural = 'Anggota Tim'


class TeamMember(models.Model):
    """
        Merupakan model database untuk menyimpan data anggota salah satu
        tim yang mengikuti sebuah kompetisi.
    """

    # Relationship dengan id tim dimana anggota tim berada
    team = models.ForeignKey(
        to=HackathonTeams, related_name='member_to_team', on_delete=models.CASCADE
    )

    # Attribut umum user
    nama_lengkap = models.CharField(max_length=100)
    email = models.EmailField(_('email address'))
    nomor_identitas = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(default=None)
    alamat = models.CharField(max_length=250)

    # Attribut kontak user
    id_line = models.CharField(max_length=30)
    nomor_telepon = models.CharField(max_length=13)


class TaskResponse(models.Model):
    WAITING = 'menunggu_verifikasi'
    DONE = 'selesai'
    REJECTED = 'ditolak'
    STATUS_CHOICES = (
        (WAITING, 'Menunggu Verifikasi'),
        (DONE, 'Selesai'),
        (REJECTED, 'Ditolak'),
    )

    task = models.ForeignKey(
        to=HackathonTask, related_name='task_response', on_delete=models.PROTECT)
    team = models.ForeignKey(
        to=HackathonTeams, related_name='task_response', on_delete=models.CASCADE)
    response = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.task.name, self.team.name)

    def save(self, *args, **kwargs):
        if self.pk is None and (self.status is None or self.status == ''):
            if self.task.require_validation:
                self.status = self.WAITING
                self.is_verified = False
            else:
                self.status = self.DONE
                self.is_verified = True

            # if self.task.task_type == HackathonTask.PAYMENT_SUBMISSION:
            #     Thread(target=self.send_email_p).start()

            # if self.task.track.pk != self.team.track.pk:
            # raise ValidationError('Track Kompetisi dan Track Tim haruslah sama.')
            # else:

        super(TaskResponse, self).save(*args, **kwargs)

    def send_line_notification(self):
        auth_token = 'JrtU8tFBrOugQLboQvaFpJdjlM5EvRIwUWaIwNwhGD5N6q1KcaouIgKd20VsJnNlQxc0RcBEf8nahzX6vJw9e51VcWA6BcQV+/F1PHNb5KVOGWxvvhM5CVyAx52RqInxmQGWQe8AToPTXLte/QUhUQdB04t89/1O/w1cDnyilFU='
        hed = {'Authorization': 'Bearer ' + auth_token}
        data = {
            "to": "C0fd8ac3ed9f41fe84d3de2d7581d52ed",
            "messages": [
                {
                    "type": "text",
                    "text": "[INFO TASK]\n{} baru saja mengunggah file di {}.".format(self.team.name, self.task.name)
                }
            ]
        }

        url = 'https://api.line.me/v2/bot/message/push'

        requests.post(url, json=data, headers=hed)

    def send_email_p(self):
        context = {
            'nama_acara': self.task.track.name,
            'nama_tim': self.team.name
        }

        text_template = get_template('up_pembayaran.html')
        html_template = get_template('up_pembayaran.html')
        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)
        mail = EmailMultiAlternatives(
            subject='Pembayaran kamu sedang diverifikasi - IFest #8',
            body=mail_text_message,
            to=[self.team.team_leader.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

    def send_email_tolak(self):
        context = {
            'nama_tugas': self.task.name,
            'nama_tim': self.team.name
        }

        text_template = get_template('submisi_ditolak.html')
        html_template = get_template('submisi_ditolak.html')
        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)
        mail = EmailMultiAlternatives(
            subject='Submisi Tugas {} - {} Ditolak - IFest #8'.format(
                self.task.name, self.team.name),
            body=mail_text_message,
            to=[self.team.team_leader.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

    def send_email_pembayaran_selesai(self):
        context = {
            'nama_kompetisi': self.task.track.name,
            'nama_tim': self.team.name,
            'jumlah': '{:20,.2f}'.format(self.task.track.biaya_pendaftaran),
            'tanggal': datetime.datetime.now().strftime("%d %B %Y %I:%M:%S %p"),
            'nama_ketua': self.team.team_leader,
            'asal_institusi': self.team.institution
        }

        text_template = get_template('bayar_valid.html')
        html_template = get_template('bayar_valid.html')
        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)
        mail = EmailMultiAlternatives(
            subject='Pembayaran kamu telah diverifikasi - IFest #8',
            body=mail_text_message,
            to=[self.team.team_leader.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

    class Meta:
        unique_together = (('task', 'team'),)
        get_latest_by = 'created_at'
        verbose_name = 'Respon Task Tim'
        verbose_name_plural = 'Respon Task Tim'

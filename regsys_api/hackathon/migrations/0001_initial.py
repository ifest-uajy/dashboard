# Generated by Django 2.2.7 on 2019-11-17 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonTask',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('deadline', models.DateTimeField(null=True)),
                ('task_type', models.CharField(choices=[
                 ('upload file', 'Uploader File'), ('pengumuman', 'Pengumuman')], max_length=50)),
                ('require_validation', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Task Lomba',
                'verbose_name_plural': 'Task Lomba',
            },
        ),
        migrations.CreateModel(
            name='HackathonTeams',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('institution', models.CharField(max_length=100)),
                ('alamat_institusi', models.CharField(max_length=500)),
                ('nama_pendamping', models.CharField(max_length=50)),
                ('nomor_telepon_pendamping', models.CharField(max_length=20)),
                ('invitation_token', models.CharField(
                    default='comma-groom-audio-sediment', max_length=100)),
                ('is_blacklisted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                                   related_name='active', to='hackathon.HackathonTask')),
            ],
            options={
                'verbose_name': 'Tim',
                'verbose_name_plural': 'Tim',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('closed_date', models.DateTimeField(null=True)),
                ('team_max_member', models.IntegerField(default=1)),
                ('team_min_member', models.IntegerField(default=1)),
                ('slug_name', models.CharField(max_length=50)),
                ('biaya_pendaftaran', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Kompetisi',
                'verbose_name_plural': 'Kompetisi',
            },
        ),
        migrations.CreateModel(
            name='HackathonTeamsMember',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='team_members', to='hackathon.HackathonTeams')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                           related_name='team_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anggota Tim',
                'verbose_name_plural': 'Anggota Tim',
                'get_latest_by': 'created_at',
                'unique_together': {('team', 'user')},
            },
        ),
        migrations.AddField(
            model_name='hackathonteams',
            name='members',
            field=models.ManyToManyField(
                related_name='teams', through='hackathon.HackathonTeamsMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hackathonteams',
            name='team_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='team_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hackathonteams',
            name='track',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='hackathon.Track'),
        ),
        migrations.AddField(
            model_name='hackathontask',
            name='track',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='hackathon.Track'),
        ),
        migrations.CreateModel(
            name='TaskResponse',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('status', models.CharField(choices=[('menunggu_verifikasi', 'Menunggu Verifikasi'), (
                    'selesai', 'Selesai'), ('ditolak', 'Ditolak')], max_length=50)),
                ('updated_at', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('is_verified', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                           related_name='task_response', to='hackathon.HackathonTask')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='task_response', to='hackathon.HackathonTeams')),
            ],
            options={
                'verbose_name': 'Respon Task Tim',
                'verbose_name_plural': 'Respon Task Tim',
                'get_latest_by': 'created_at',
                'unique_together': {('task', 'team')},
            },
        ),
    ]

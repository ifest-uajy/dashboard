# Generated by Django 2.2.4 on 2019-08-24 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0004_remove_hackathonteam_team_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonTeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('institution', models.CharField(max_length=100)),
                ('is_blacklisted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HackathonTeamsMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='hackathon.HackathonTeams')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_at',
                'unique_together': {('team', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team_max_member', models.IntegerField(default=1)),
                ('team_min_member', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='hackathonuser',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='hackathonuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='HackathonTeam',
        ),
        migrations.DeleteModel(
            name='HackathonUser',
        ),
        migrations.AddField(
            model_name='hackathonteams',
            name='members',
            field=models.ManyToManyField(related_name='teams', through='hackathon.HackathonTeamsMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hackathonteams',
            name='team_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hackathonteams',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='hackathon.Track'),
        ),
    ]

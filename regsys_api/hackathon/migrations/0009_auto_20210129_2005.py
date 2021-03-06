# Generated by Django 2.2.7 on 2021-01-29 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathon', '0008_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnggotaTim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('identity_number', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('line_id', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]

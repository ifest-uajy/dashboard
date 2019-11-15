from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (
    HackathonTask,
    HackathonTeamsMember,  # done
    HackathonTeams,  # done
    TaskResponse,
    Track  # done
)
from regsys_api.authsys.models import User


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'team_min_member',
                    'team_max_member', 'description', 'closed_date', 'biaya_pendaftaran']


@admin.register(HackathonTeamsMember)
class HackathonUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'created_at']

    ordering = ['created_at']


@admin.register(TaskResponse)
class TaskResponseAdmin(admin.ModelAdmin):
    list_display = [
        'task', 'team', 'response', 'status', 'updated_at', 'announcement_title', 'announcement_desc', 'file_path', 'is_verified'
    ]

    ordering = ['updated_at']


@admin.register(HackathonTask)
class HackathonTaskAdmin(admin.ModelAdmin):
    list_display = [
        'track', 'name', 'order', 'deadline', 'require_validation', 'task_type'
    ]

    ordering = ['track', 'order', '-deadline']


@admin.register(HackathonTeams)
class HackathonTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'track', 'institution', 'show_team_leader', 'get_members',
                    'team_members_count',
                    'current_task',
                    'is_blacklisted', 'created_at']
    search_fields = ['name', 'institution']
    list_filter = ['created_at']

    def get_members(self, obj):
        return ", ".join([p.full_name for p in obj.members.all()])

    def show_team_leader(self, obj):
        return '%s (%s)' % (obj.team_leader.full_name, obj.team_leader.email)

    def team_members_count(self, obj):
        return obj.members.all().count()

    ordering = ['track', 'name']

    team_members_count.short_description = 'Jumlah Peserta'
    get_members.short_description = 'List Anggota Tim'
    show_team_leader.short_description = 'Ketua Tim'

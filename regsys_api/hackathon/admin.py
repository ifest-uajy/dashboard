from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (
    HackathonTask,
    HackathonTeamsMember,  # done
    HackathonTeams,  # done
    TaskResponse,
    Track,  # done
)
from regsys_api.authsys.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib import messages
from threading import Thread


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'team_min_member',
                    'team_max_member', 'description', 'closed_date', 'biaya_pendaftaran',
                    'is_shown', 'slug_image']


@admin.register(HackathonTeamsMember)
class HackathonUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'team', 'created_at']

    ordering = ['created_at']


@admin.register(TaskResponse)
class TaskResponseAdmin(admin.ModelAdmin):
    list_display = [
        'task', 'team', 'response', 'download_response_actions', 'status', 'updated_at', 'is_verified', 'task_response_actions', 'tolak_response'
    ]

    ordering = ['updated_at']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<task_res_id>.+)/verify/$',
                self.admin_site.admin_view(self.process_verify),
                name='verify',
            ),
            url(
                r'^(?P<task_res_id>.+)/tolak/$',
                self.admin_site.admin_view(self.process_reject),
                name='tolak',
            ),
        ]
        return custom_urls + urls

    def download_response_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Download</a>&nbsp;',
            '/api/file/download/' + obj.response + '/',
        )
    download_response_actions.short_description = "Download tugas tim"
    download_response_actions.allow_tags = True

    def task_response_actions(self, obj):
        if(obj.is_verified is False and obj.status != TaskResponse.REJECTED):
            return format_html(
                '<a class="button" href="{}">Verif</a>&nbsp;',
                reverse('admin:verify', args=[obj.pk]),
                )
    task_response_actions.short_description = 'Verif Respon'
    task_response_actions.allow_tags = True

    def tolak_response(self, obj):
        if(obj.task.require_validation and obj.is_verified is False and obj.status != TaskResponse.REJECTED):
            return format_html(
                '<a class="button" href="{}">Tolak</a>&nbsp;',
                reverse('admin:tolak', args=[obj.pk]),
                )
    tolak_response.short_description = 'Tolak Respon'
    tolak_response.allow_tags = True

    def process_verify(self, request, task_res_id, *args, **kwargs):
        return self.process_action(
            request=request,
            task_res_id=task_res_id,
        )

    def process_reject(self, request, task_res_id, *args, **kwargs):
        return self.process_action_reject(
            request=request,
            task_res_id=task_res_id,
        )

    def process_action_reject(self, request, task_res_id):

        if request.user.has_perm('hackathon.change_taskresponse'):

            task = self.get_object(request, task_res_id)

            task.is_verified = False

            task.status = TaskResponse.REJECTED
            Thread(target=task.send_email_tolak).start()
            task.save()
            messages.info(
                request, 'Task untuk {} ditolak, terimakasih'.format(task.team.name))

        else:
            messages.error(request, 'tidak ada permision untuk melakukan ini')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj=obj)

    def process_action(self, request, task_res_id):

        if request.user.has_perm('hackathon.change_taskresponse'):

            task = self.get_object(request, task_res_id)

            task.is_verified = True

            task.status = TaskResponse.DONE

            if task.task.task_type == HackathonTask.PAYMENT_SUBMISSION:
                Thread(target=task.send_email_pembayaran_selesai).start()

            task.save()
            task.team.move_one_step()
            messages.info(
                request, 'Task untuk {} sudah di verifikasi, terimakasih'.format(task.team.name))

        else:
            messages.error(request, 'tidak ada permision untuk melakukan ini')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@admin.register(HackathonTask)
class HackathonTaskAdmin(admin.ModelAdmin):
    list_display = [
        'track', 'name', 'order', 'deadline', 'require_validation', 'task_type', 'max_file_upload'
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

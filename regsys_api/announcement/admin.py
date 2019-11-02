from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Announcement
from regsys_api.authsys.models import User
from django import forms

class AnnouncementForm( forms.ModelForm ):
    message = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Announcement
        fields = ('__all__')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'issuer',
        'issued_at',
        'type',
        'isShown'
    ]
    search_fields = ['title']
    ordering = ['issued_at']
    form = AnnouncementForm
    
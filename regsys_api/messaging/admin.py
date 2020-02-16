from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Message
from django import forms

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'nama_pengirim',
        'email_pengirim',
        'pesan',
        'recieved_at',
        'replied'
    ]

    ordering = ['-recieved_at', '-replied']

    readonly_fields = [
        'nama_pengirim',
        'email_pengirim',
        'pesan',
        'recieved_at'
    ]

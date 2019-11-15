from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import PersonalUploadFile, TeamUploadFile
from regsys_api.authsys.models import User
import uuid

@admin.register(PersonalUploadFile)
class PersonalUploadFileAdmin(admin.ModelAdmin):
    list_display=['file_download', 'id', 'original_filename', 'file_size', 'uploaded_by', 'uploaded_at']
    list_display_links = ['id', 'original_filename']
    search_fields = ['original_filename', 'uploaded_by']
    readonly_fields = ['file_download', 'id', 'file_size']
    autocomplete_fields = ['uploaded_by']

    def file_download(self, instance):
        link = reverse('download', kwargs={'file_id': str(instance.id)})
        return format_html('<a href="{}" download="{}" target="_blank">Download</a>', link, ' ' + instance.original_filename)

    class Meta:
        ordering = ['-uploaded_at']
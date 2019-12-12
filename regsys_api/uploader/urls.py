from django.urls import path
from django.conf.urls import url
from .views import (
    PersonalUploadFileView, getDownloadView
)

urlpatterns = [
    path('upload/', PersonalUploadFileView.as_view()),
    url('^download/(?P<file_id>.+)/$', getDownloadView.as_view(), name='download'),
]
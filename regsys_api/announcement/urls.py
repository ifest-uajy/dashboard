from django.urls import path
from .views import (
    AnnouncementView
)

urlpatterns = [
    path('', AnnouncementView.as_view())
]
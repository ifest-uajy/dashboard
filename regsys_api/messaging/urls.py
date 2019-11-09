from django.urls import path
from .views import (
    MessageView
)

urlpatterns = [
    path('send/', MessageView.as_view()),
]
from rest_framework.response import Response
from django.db import transaction
from rest_framework.generics import ListAPIView
from rest_framework.views import (APIView)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import status
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
#from django.views.decorators.debug import sensitive_post_parameters
from regsys_api.authsys.models import User
from .models import (
    Announcement,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from .serializers import AnnouncementSerializer


class AnnouncementView(ListAPIView):
    queryset = Announcement.objects.filter(isShown=True)
    serializer_class = AnnouncementSerializer

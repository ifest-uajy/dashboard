"""regsys_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.decorators.cache import never_cache
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

index_view = never_cache(TemplateView.as_view(template_name='index.html'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('regsys_api.authsys.urls')),
    path('api/hackathon/', include('regsys_api.hackathon.urls')),
    path('api/announcement/', include('regsys_api.announcement.urls')),
    path('api/message/', include('regsys_api.messaging.urls')),
    path('api/file/', include('regsys_api.uploader.urls')),
    url(r'^.*$', index_view),
    #path('', index_view, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

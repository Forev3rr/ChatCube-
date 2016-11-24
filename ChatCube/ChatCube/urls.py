"""ChatCube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from chat.views import RoomViewSet, MessageViewSet
from django.views.generic.base import TemplateView
from users.views import GroupViewSet, CustomUserViewSet
from django.contrib.auth import views as auth_views
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'rooms', RoomViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/', include('users.urls')),
    url(r'^rooms/', include('chat.urls')),
]

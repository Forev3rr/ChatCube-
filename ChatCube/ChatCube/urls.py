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
from users.views import GroupViewSet, CustomUserViewSet, LoginView, LogoutView
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'groups', GroupViewSet)
# router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'rooms', RoomViewSet)


urlpatterns = [
    url(r'api/^', include(router.urls)),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', TemplateView.as_view(template_name='static/templates/authentication/login.html'), name="home"),
    # url(r'^search/', StudentViewSet.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls',
    #                            namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^auth/', include('djoser.urls.authtoken'))
]

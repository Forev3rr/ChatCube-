from django.conf.urls import url, include
from .views import index, contact

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^info/$', contact, name='info'),
]

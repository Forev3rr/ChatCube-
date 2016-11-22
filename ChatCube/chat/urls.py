from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Message, Room

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Room.objects.all().order_by("-date")[:25],
                                            template_name="chat/rooms.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Room,
                                                         template_name = 'chat/room.html'))
                ]

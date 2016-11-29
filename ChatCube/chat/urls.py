from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Message, Room
from .views import aroom

class RoomView(ListView):
    model = Room
    template_name = "chat/rooms.html"
    def get_queryset(self):
        return Room.objects.filter(participants=self.request.user)

urlpatterns = [ url(r'^$', RoomView.as_view(), name='rooms'),
                # url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Room,
                #                                          template_name = 'chat/room.html')),
                url(r'^(?P<pk>\d+)$', aroom, name='aroom')
]
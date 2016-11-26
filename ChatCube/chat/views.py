from rest_framework import viewsets
from .models import Room, Message, MessageForm
from .serializers import RoomSerializer, MessageSerializer
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib import messages


def aroom(request, pk):
    room = Room.objects.get(pk=pk)
    messages = Message.objects.filter(targets=room)
    mess = []
    for m in messages:
        mess.append(m.message)
    if request.method == 'POST':
        # form = MessageForm(request.POST)
        # print form
        # if form.is_valid():
        #     instance = form.save(commit=False)
        # instance.targets = room
        # instance.sender = request.user
        message = request.POST.get('message', '')
        message_obj = Message(message=message, sender=request.user, targets=room)
        message_obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'chat/room.html', {'content':[room.name, mess]})

class RoomViewSet(viewsets.ModelViewSet):
    model = Room
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
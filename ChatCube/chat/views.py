from rest_framework import viewsets
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

class RoomViewSet(viewsets.ModelViewSet):
    model = Room
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
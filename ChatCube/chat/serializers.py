from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id',
                  'name',
                  'password',
                  'owner',
                  'participants',)
        view_name = 'room-detail'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message',
                  'sender',
                  'targets',)
        view_name = 'message-detail'

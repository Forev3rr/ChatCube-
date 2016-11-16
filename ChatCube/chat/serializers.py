from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id',
                  'name',
                  'password',
                  'owner',
                  'participants',
                  'message_set')
        view_name = 'room-detail'


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('message',
                  'sender',
                  'targets',)
        view_name = 'message-detail'

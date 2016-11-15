from django.contrib import admin
from .models import (Message,
                     Room)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message',
                    'sender',
                    'targets')
    search_fields = ['message',
                     'sender']

admin.site.register(Message, MessageAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'password',
                    'participants')
    search_fields = ['name',
                     'participants']

admin.site.register(Room, RoomAdmin)


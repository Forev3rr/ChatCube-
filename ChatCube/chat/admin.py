from django.contrib import admin
from .models import (Message,
                     Room)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message',
                    'sender')
    search_fields = ['message',
                     'sender']

admin.site.register(Message, MessageAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Room, RoomAdmin)


from django.contrib import admin
from .models import (Message,
                     Room)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message',
                    'sender',
                    'targets')
    list_filter = ('targets',)
    search_fields = ['targets',
                     'sender']

admin.site.register(Message, MessageAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'owner')
    search_fields = ['name',
                     'owner']
    list_filter = ('owner',)


admin.site.register(Room, RoomAdmin)


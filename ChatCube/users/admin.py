from django.contrib import admin
from .models import (CustomUser,
                     Group)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'auth_level')
    search_fields = ['username',
                     'auth_level']

admin.site.register(CustomUser, CustomUserAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'password')
    search_fields = ['name',
                     'password']

admin.site.register(Group, GroupAdmin)


from django.contrib import admin
from .models import (CustomUser,
                     Group)
from django.contrib.auth.admin import UserAdmin
from django import forms

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    ordering = ("username",)
    list_display = ('username', 'email')
    search_fields = ['username', 'email']
    fieldsets = (
          ('Personal info', {
              'fields': ('username',
                         'password',
                         'email',)
          }),
          ('Internal info', {
              'fields': ('is_staff',
                         'is_superuser',
                         'is_active',
                         )

          }),
       )
    add_fieldsets = fieldsets
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username',
#                     'auth_level')
#     search_fields = ['username',
#                      'auth_level']
#
# admin.site.register(CustomUser, CustomUserAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'password')
    search_fields = ['name',
                     'password']

admin.site.register(Group, GroupAdmin)


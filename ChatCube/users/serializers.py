from rest_framework import serializers
from .models import Group, CustomUser
from django.contrib.auth import update_session_auth_hash


class CustomUserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=False)
    # confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('id',
                  'username',
                  'email',
                  'auth_level',
                  'is_active',)
        view_name = 'customuser-detail'

        # def create(self, validated_data):
        #     return CustomUser.objects.create(**validated_data)
        #
        # def update(self, instance, validated_data):
        #     instance.username = validated_data.get('username', instance.username)
        #     instance.save()
        #     password = validated_data.get('password', None)
        #
        #     instance.set_password(password)
        #     instance.save()
        #
        #     update_session_auth_hash(self.context.get('request'), instance)
        #
        #     return instance

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',
                  'password',
                  'users',)
        view_name = 'group-detail'

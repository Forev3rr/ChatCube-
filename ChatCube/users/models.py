from __future__ import unicode_literals
import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.core import validators
from django.utils.http import urlquote

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.is_staff = True
        account.is_superuser=True
        account.save()
        return account

    # def _create_user(self, username, email, password,
    #                  is_staff, is_superuser, **extra_fields):
    #     """
    #     Creates and saves a User with the given email and password.
    #     """
    #     now = timezone.now()
    #     if not email:
    #         raise ValueError('The given email must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(username=username, email=email,
    #                       is_staff=is_staff, is_active=True,
    #                       is_superuser=is_superuser, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, username, email, password=None, **extra_fields):
    #     return self._create_user(username, email, password, False, False,
    #                              **extra_fields)
    #
    # def create_superuser(self, username, email, password, **extra_fields):
    #     return self._create_user(username, email, password, True, True,
    #                              **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username \
        = models.CharField(max_length=30,
                           unique=True,
                           help_text=('Required. 30 characters or fewer. '
                                      'Letters, numbers and _ character'),
                           validators=[
                               validators.RegexValidator(re.compile('^[\w]+$'),
                                                         'Enter a'
                                                         ' valid username.',
                                                         'invalid')],
                           error_messages={
                                'unique': "A user with that username "
                                "already exists.", }
                           )
    email = models.EmailField(max_length=254)
    auth_level = models.IntegerField(default=1)
    is_staff = models.BooleanField(default=False,
                                   help_text=('Designates whether the user can'
                                              ' log into this admin site. '
                                              'Should be reserved for singolar'
                                              ' employees.'))
    is_active = models.BooleanField(default=True,
                                    help_text=('Designates whether this user '
                                               'is online.'))

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # def get_absolute_url(self):
    #     return "/users/%s/" % urlquote(self.username)

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

class User(models.Model):
    # auto Id
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    auth_level = models.IntegerField(default=1)
    # picture =
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Group(models.Model):
    # auto Id
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    users = models.ForeignKey(CustomUser,
                              on_delete=models.CASCADE,
                              related_name='users')

    def __str__(self):
        return self.name




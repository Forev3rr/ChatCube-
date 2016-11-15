from __future__ import unicode_literals
from django.db import models
from users.models import User

# Create your models here.

class Room(models.Model):
    # auto Id
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    owner = models.ForeignKey(User,
                              related_name='owner',
                              default=1,)
    participants = models.ForeignKey(User,
                              related_name='participants',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Message(models.Model):
    # auto Id
    message = models.TextField(blank=True)
    sender = models.ForeignKey(User,
                               related_name='sender',
                               default=1,)
    targets = models.ForeignKey(User,
                               default=1,
                               related_name='targets',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.message

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-15 19:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20161115_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='targets',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='targets', to=settings.AUTH_USER_MODEL),
        ),
    ]

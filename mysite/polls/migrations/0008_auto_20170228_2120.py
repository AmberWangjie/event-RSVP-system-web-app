# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_event_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='event',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='guest',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 01:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170228_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='data',
        ),
    ]

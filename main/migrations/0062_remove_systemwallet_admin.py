# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_auto_20171114_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemwallet',
            name='admin',
        ),
    ]

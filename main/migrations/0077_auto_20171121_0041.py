# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 16:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0076_auto_20171121_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20171027_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='available_time',
        ),
        migrations.AddField(
            model_name='availability',
            name='tutor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Tutor'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0089_auto_20171123_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='numReviews',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

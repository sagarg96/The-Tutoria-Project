# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20171028_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Tutor'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 16:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0100_auto_20171124_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phoneNo',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phoneNo',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
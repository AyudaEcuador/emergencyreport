# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-01 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericform', '0008_auto_20170601_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericoption',
            name='label',
            field=models.CharField(max_length=50),
        ),
    ]

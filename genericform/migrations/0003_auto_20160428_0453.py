# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genericform', '0002_auto_20160428_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericoption',
            name='genericparentoption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='genericform.GenericParentOption'),
        ),
        migrations.AlterField(
            model_name='genericparentoption',
            name='genericfield',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='options_parent', to='genericform.GenericField'),
        ),
        migrations.AlterField(
            model_name='genericparentoption',
            name='tipo',
            field=models.IntegerField(choices=[(1, b'NUMERICO'), (2, b'TEXTO')]),
        ),
    ]

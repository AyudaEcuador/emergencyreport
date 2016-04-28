# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genericform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genericfield',
            old_name='nombre',
            new_name='verbose_name',
        ),
        migrations.RemoveField(
            model_name='genericfield',
            name='tipo',
        ),
        migrations.AddField(
            model_name='genericfield',
            name='help_text',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genericfield',
            name='read_only',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genericfield',
            name='required',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genericfield',
            name='type',
            field=models.IntegerField(choices=[(1, b'TEXTO_SOLO_NUMEROS_ENTEROS'), (2, b'TEXTO_SOLO_DECIMALES'), (3, b'TEXTO_SOLO_LETRAS'), (4, b'TEXTO_SOLO_LETRAS_Y_NUMEROS'), (5, b'TEXTO_SOLO_LETRAS_CON_ESPACIOS'), (6, b'TEXTO_SOLO_LETRAS_Y_NUMEROS_CON_ESPACIOS'), (7, b'TEXTO_SOLO_LETRAS_Y_NUMEROS_CON_ESPACIOS_Y_SIMBOLOS'), (8, b'SELECCIONABLE_TEXTO')], default=1),
            preserve_default=False,
        ),
    ]
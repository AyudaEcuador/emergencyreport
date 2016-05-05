from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Lugar(models.Model):
    LUGAR_CHOICES = (
        (1, 'Refugio'),
        (2, 'albergue'),
        (3, 'campamento'),
    )

    nombre = models.CharField(max_length=64)
    tipo = models.IntegerField(choices=LUGAR_CHOICES)


class Perfil(models.Model):
    usuario = models.ForeignKey(User)
    lugar = models.ForeignKey(Lugar)
    telefono = models.CharField(max_length=15)

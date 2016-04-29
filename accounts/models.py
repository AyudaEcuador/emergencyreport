from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Institucion(models.Model):
    nombre = models.CharField(max_length=64)


class Perfil(models.Model):
    usuario = models.ForeignKey(User)
    institucion = models.ForeignKey(Institucion)
    telefono = models.CharField(max_length=15)



from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    alternative_login = models.CharField(max_length=15)
    alternative_pin = models.CharField(max_length=200)

# class Institucion(models.Model):
#     nombre = models.CharField(max_length=64)
#
#
# class Perfil(models.Model):
#     usuario = models.ForeignKey(User)
#     institucion = models.ForeignKey(Institucion)
#     telefono = models.CharField(max_length=15)
#
#
#

from django.db import models

# Create your models here.
class GenericForm(models.Model):
    nombre_corto = models.CharField(max_length=150)
    mesa = models.IntegerField()
    ordinal = models.IntegerField()
    hora_entrega = models.TimeField()
    descripcion = models.TextField()

    def __unicode__(self):
        return str(self.nombre_corto)

    class Meta:
        pass


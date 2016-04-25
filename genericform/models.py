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


class GenericField(models.Model):
    TIPO_CHOICES = (
        (1, 'NUMERICO'),
        (2, 'TEXTO'),
        (3, 'SELECCIONABLE_TEXTO'),
    )

    genericform = models.ForeignKey(GenericForm)
    nombre =  models.CharField(max_length=20)
    ordinal = models.IntegerField()
    tipo = models.IntegerField(choices=TIPO_CHOICES)
    validation_dict = models.TextField()

    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        pass

class GenericParentOption(models.Model):
    TIPO_CHOICES = (
        (1, 'NUMERICO'),
        (2, 'TEXTO'),
        (3, 'VERDADERO/FALSO')
    )
    genericfield = models.ForeignKey(GenericField)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        pass


class GenericOption(models.Model):
    TIPO_CHOICES = (
        (1, 'NUMERICO'),
        (2, 'TEXTO'),
        (3, 'VERDADERO/FALSO')
    )
    genericfield = models.ForeignKey(GenericField)
    nombre = models.CharField(max_length=15)
    valor = models.CharField(max_length=20,help_text='El valor del campo sera convertido')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        pass

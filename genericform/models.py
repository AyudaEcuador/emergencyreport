from django.db import models
from django.contrib.postgres.fields import JSONField


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
        (1, 'TEXTO_SOLO_NUMEROS_ENTEROS'),
        (2, 'TEXTO_SOLO_DECIMALES'),
        (3, 'TEXTO_SOLO_LETRAS'),
        (4, 'TEXTO_SOLO_LETRAS_Y_NUMEROS'),
        (5, 'TEXTO_SOLO_LETRAS_CON_ESPACIOS'),
        (6, 'TEXTO_SOLO_LETRAS_Y_NUMEROS_CON_ESPACIOS'),
        (7, 'TEXTO_SOLO_LETRAS_Y_NUMEROS_CON_ESPACIOS_Y_SIMBOLOS'),
        (8, 'SELECCIONABLE_TEXTO'),
    )

    genericform = models.ForeignKey(GenericForm, related_name='fields')
    verbose_name = models.CharField(max_length=20)
    ordinal = models.IntegerField()
    type = models.IntegerField(choices=TIPO_CHOICES)
    help_text = models.CharField(max_length=128)
    required = models.BooleanField()
    read_only = models.BooleanField()
    validation_dict = models.TextField()

    def __unicode__(self):
        return unicode(self.verbose_name)

    @property
    def options(self):
        if self.options_type:
            return self.options_type.options

    class Meta:
        pass


class GenericParentOption(models.Model):
    TIPO_CHOICES = (
        (1, 'NUMERICO'),
        (2, 'TEXTO'),
    )
    genericfield = models.OneToOneField(GenericField, related_name='options_type')
    tipo = models.IntegerField(choices=TIPO_CHOICES)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        pass


class GenericOption(models.Model):
    genericparentoption = models.ForeignKey(GenericParentOption, related_name='options')
    label = models.CharField(max_length=15)
    value = models.CharField(max_length=20, help_text='El valor del campo sera convertido')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        pass


class GenericFormData(models.Model):
    form = models.ForeignKey(GenericForm)
    data = models.TextField()

    def __unicode__(self):
        return str(self.id)


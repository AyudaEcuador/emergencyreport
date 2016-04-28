from rest_framework import serializers
from . import models


class GenericOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GenericOption
        fields = ('label', 'value')


class GenericFieldSerializer(serializers.ModelSerializer):
    options = GenericOptionSerializer(many=True)
    type = serializers.SerializerMethodField()

    def get_type(self, field):
        return field.get_type_display()

    class Meta:
        model = models.GenericField
        fields = ('verbose_name', 'ordinal', 'type', 'help_text', 'required',
                  'read_only', 'options', 'validation_dict')


class GenericFormSerializer(serializers.ModelSerializer):
    fields = GenericFieldSerializer(many=True)

    class Meta:
        model = models.GenericForm
        fields = ('nombre_corto', 'mesa', 'ordinal', 'hora_entrega',
                  'descripcion', 'fields')

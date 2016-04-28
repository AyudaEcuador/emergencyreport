from rest_framework import generics
from . import models
from . import serializers


class FormMetadataView(generics.RetrieveAPIView):
    queryset = models.GenericForm.objects.all()
    serializer_class = serializers.GenericFormSerializer

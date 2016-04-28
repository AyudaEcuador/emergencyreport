from rest_framework import generics
from rest_framework import views
from rest_framework import response
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from . import models
from . import serializers


class FormMetadataView(generics.RetrieveAPIView):
    queryset = models.GenericForm.objects.all()
    serializer_class = serializers.GenericFormSerializer


class FormDataView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, form, format=None):
        models.GenericFormData.objects.create(
            form_id=form, data=request.data)
        return response.Response({})




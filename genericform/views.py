from rest_framework import generics
from rest_framework import views
from rest_framework import response
from rest_framework import permissions
from django.shortcuts import render_to_response, HttpResponse, render
from . import models
from . import serializers
from models import Mesa, GenericForm


def formularios_por_mesa(request,mesa_id):
     print 'hola'
     dict = {}
     dict['formularios_list'] = GenericForm.objects.filter(mesa_id = mesa_id)
     dict['mesa_id'] = mesa_id
     print len ( dict['formularios_list'])
     print 'filter'
     return render(request, 'genericreport/sel_form.html', dict)






def mesas(request):
     dict = {}
     dict['mesas_list'] = Mesa.objects.filter()

     print len(dict['mesas_list'])
     return render(request, 'genericreport/sel_mesa.html', dict)



class FormMetadataView(generics.RetrieveAPIView):
    queryset = models.GenericForm.objects.all().order_by('-genericfield__ordinal')
    serializer_class = serializers.GenericFormSerializer


class FormDataView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, form, format=None):
        models.GenericFormData.objects.create(
            form_id=form, data=request.data)

        print request.data['']


        return response.Response({})



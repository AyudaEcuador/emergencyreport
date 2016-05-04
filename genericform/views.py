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
     dict['mesas_list'] = Mesa.objects.filter().order_by('numero_mesa')

     print len(dict['mesas_list'])
     return render(request, 'genericreport/sel_mesa.html', dict)



class FormMetadataView(generics.RetrieveAPIView):
    queryset = models.GenericForm.objects.all().order_by('-genericfield__ordinal')
    serializer_class = serializers.GenericFormSerializer


class FormDataView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, form, format=None):
        obj = models.GenericFormData.objects.create(
            form_id=form, data=request.data)



        redirect_url = "/mesa/" + str(obj.form.mesa.id) + "/reportes/"
        mensaje = "El formulario " + str(obj.form.ordinal) + " de la mesa " + str(obj.form.mesa.numero_mesa) + " se grabo correctamente."

        return response.Response({'saved_id':obj.id,'redirect_url':redirect_url,'mensaje':mensaje})



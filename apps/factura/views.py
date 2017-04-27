import json
from rest_framework.views import APIView
#from apps.historia.serializers import CurvaSerializers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.factura.forms import FacturaForm
from apps.factura.models import Factura
from apps.cliente.models import Cliente
from apps.empresa.models import Empresa_a
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers 
#Instalar para campo de formulario con fecha
#https://github.com/nkunihiko/django-bootstrap3-datetimepicker



#----------Vista para  las historias 

class factura_view(CreateView):
    
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/factura_create.html'
    success_url = reverse_lazy('cliente:cliente_listar')    
    
class factura_edit(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/factura_create.html'
    success_url = reverse_lazy('cliente:cliente_listar')
    

class factura_list(ListView):
    
    model = Factura
    template_name = 'factura/factura_mostrar.html'
    def get_queryset(self):
      
       return Factura.objects.get(pk=self.kwargs['pk'])
    
    
      
    
    
    def get_context_data(self,  **kwargs):
                
        context=super(factura_list,self).get_context_data(**kwargs)
        context['cliente']=Cliente.objects.filter(factura__id=self.kwargs['pk'])
        context['empresa']=Empresa_a.objects.filter(id='2')
        return context
        
    
    
        
    
#class Curva_crecimiento(APIView):
#    serializer = CurvaSerializers
    
#   def get(self, request,format=None, **kwargs):
#      curva =  Historia.objects.filter(pacientes__pk=self.kwargs['pk'])
#     response= self.serializer(curva,many=True)
#    return HttpResponse(json.dumps(response.data), content_type='application/json')
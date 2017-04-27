from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.cliente.forms import ClienteForm
from apps.cliente.models import Cliente
from apps.factura.models import Factura
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.core  import serializers 
#Instalar para campo de formulario con fecha
#https://github.com/nkunihiko/django-bootstrap3-datetimepicker

def index(request):
    return render(request, 'cliente/index.html')

#---------------------------------Vistar para crear editar y borrar pacientes  
    
class cliente_view(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')
   

class cliente_list(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    success_url = reverse_lazy('cliente:cliente_listar')
    

class cliente_mostrar(ListView):
    model = Cliente
   
    success_url = reverse_lazy('cliente:cliente_listar')
    def post(self, request, *args, **kwargs ):
        buscar = request.POST['cliente']
        bcliente =  Cliente.objects.filter(empresa__contains=buscar)
        
        datos = []
        
        for cliente in bcliente:
            factura = Factura.objects.filter(clientes__empresa__icontains=buscar)
            datos.append(dict([(cliente,factura)]))
            
        
        return render(request,'cliente/cliente_mostrar.html', {'datos':datos})
 
class cliente_edit(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')
    
    
class cliente_delete(UpdateView):
    model = Cliente
    form_class = Cliente
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente:cliente_listar')


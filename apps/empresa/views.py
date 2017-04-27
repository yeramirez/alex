from django.shortcuts import render
from django.http import HttpResponse
from apps.empresa.models import Empresa_a
from apps.empresa.forms import EmpresaForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class Empresa_Crear(CreateView):
    model = Empresa_a
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('empresa:empresa_listar')

class Empresa_list(ListView):
    model = Empresa_a
    form_class = EmpresaForm
    template_name = 'empresa/empresa_list.html'
    success_url = reverse_lazy('empresa:empresa_listar')
    
class Empresa_edit(UpdateView):
    model = Empresa_a
    form_class = EmpresaForm
    template_name = 'empresa/empresa_profile.html'
    success_url = reverse_lazy('empresa:empresa_listar')
    
class Empresa_delete(DeleteView):
    model = Empresa_a
    form_class = EmpresaForm
    template_name = 'empresa/empresa_delete.html'
    success_url = reverse_lazy('empresa:empresa_listar')
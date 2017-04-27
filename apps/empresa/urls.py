from django.conf.urls import url, include
from apps.empresa.views import Empresa_Crear,Empresa_list,Empresa_edit,Empresa_delete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    
    url(r'^registrar$', login_required(Empresa_Crear.as_view()), name='empresa_crear'),
    url(r'^listar$', Empresa_list.as_view(), name='empresa_listar'),
    url(r'^editar/(?P<pk>\d+)/$', Empresa_edit.as_view(), name='empresa_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', Empresa_delete.as_view(), name='empresa_eliminar'),
   
]

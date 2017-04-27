from django.conf.urls import url, include
from apps.cliente.views import index, cliente_view,cliente_list,cliente_edit,cliente_delete,cliente_mostrar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    url(r'^nuevo$', login_required(cliente_view.as_view()), name='cliente_crear'),
    
    url(r'^mostrar$',login_required( cliente_mostrar.as_view()), name='cliente_mostrar'),
    
    url(r'^listar$', login_required(cliente_list.as_view()), name='cliente_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(cliente_edit.as_view()), name='cliente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(cliente_delete.as_view()), name='cliente_eliminar'),
]
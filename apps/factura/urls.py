from django.conf.urls import url, include
from apps.factura.views import  factura_view, factura_edit,factura_list#,Curva_crecimiento
from apps.cliente.views import cliente_list
# At the top of your urls.py file, add the following line:
from django.conf import settings
from django.contrib.auth.decorators import login_required
# UNDERNEATH your urlpatterns definition, add the following two lines:

        
urlpatterns = [
   
    url(r'^nuevo$',login_required( factura_view.as_view()), name='factura_crear'),
    url(r'^list/(?P<pk>\d+)/$',login_required( factura_list.as_view()), name='factura_list'),
    #url(r'^curva/(?P<pk>\d+)/$',login_required( Curva_crecimiento.as_view()), name='curva_crecimiento'),
     
    ]
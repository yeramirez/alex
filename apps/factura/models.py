from django.db import models

from django.db import models
from apps.empresa.models import Empresa_a
from apps.cliente.models import Cliente

class Factura(models.Model):
    miempresa=models.ForeignKey(Empresa_a, null=True, blank=True, on_delete=models.CASCADE)
    clientes=models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    
    articulo = models.CharField(max_length=30,blank=True)
    cantidad = models.CharField(max_length=30,blank=True)
    precio_unitario = models.CharField(null=True,blank=True,max_length=30)
    precio_total = models.CharField(null=True,blank=True,max_length=30)
    descripcion= models.CharField(null=True,blank=True,max_length=30)
    observacion = models.TextField(null=True, blank=True)
    
    articulo1 = models.CharField(max_length=30,blank=True)
    cantidad1 = models.CharField(max_length=30,blank=True)
    precio_unitario1 = models.CharField(null=True,blank=True,max_length=30)
    precio_total1 = models.CharField(null=True,blank=True,max_length=30)
    descripcion1 = models.CharField(null=True,blank=True,max_length=30)
    observacion1 = models.TextField(null=True, blank=True)
    
    articulo2 = models.CharField(max_length=30,blank=True)
    cantidad2 = models.CharField(max_length=30,blank=True)
    precio_unitario2 = models.CharField(null=True,blank=True,max_length=30)
    precio_total2 = models.CharField(null=True,blank=True,max_length=30)
    descripcion2= models.CharField(null=True,blank=True,max_length=30)
    observacion2 = models.TextField(null=True, blank=True)
    
    
    articulo3 = models.CharField(max_length=30,blank=True)
    cantidad3 = models.CharField(max_length=30,blank=True)
    precio_unitario3 = models.CharField(null=True,blank=True,max_length=30)
    precio_total3 = models.CharField(null=True,blank=True,max_length=30)
    descripcion3 = models.CharField(null=True,blank=True,max_length=30)
    observacion3 = models.TextField(null=True, blank=True)
    
    
    articulo4 = models.CharField(max_length=30,blank=True)
    cantidad4 = models.CharField(max_length=30,blank=True)
    precio_unitario4 = models.CharField(null=True,blank=True,max_length=30)
    precio_total4 = models.CharField(null=True,blank=True,max_length=30)
    descripcion4= models.CharField(null=True,blank=True,max_length=30)
    observacion4  = models.TextField(null=True, blank=True)
    
    articulo5 = models.CharField(max_length=30,blank=True)
    cantidad5 = models.CharField(max_length=30,blank=True)
    precio_unitario5 = models.CharField(null=True,blank=True,max_length=30)
    precio_total5 = models.CharField(null=True,blank=True,max_length=30)
    descripcion5= models.CharField(null=True,blank=True,max_length=30)
    observacion5 = models.TextField(null=True, blank=True)
    
    
    articulo6 = models.CharField(max_length=30,blank=True)
    cantidad6 = models.CharField(max_length=30,blank=True)
    precio_unitario6 = models.CharField(null=True,blank=True,max_length=30)
    precio_total6 = models.CharField(null=True,blank=True,max_length=30)
    descripcion6= models.CharField(null=True,blank=True,max_length=30)
    observacion6 = models.TextField(null=True, blank=True)
    
    
    articulo7 = models.CharField(max_length=30,blank=True)
    cantidad7 = models.CharField(max_length=30,blank=True)
    precio_unitario7 = models.CharField(null=True,blank=True,max_length=30)
    precio_total7 = models.CharField(null=True,blank=True,max_length=30)
    descripcion7= models.CharField(null=True,blank=True,max_length=30)
    observacion7 = models.TextField(null=True, blank=True)
    
    articulo8 = models.CharField(max_length=30,blank=True)
    cantidad8 = models.CharField(max_length=30,blank=True)
    precio_unitario8 = models.CharField(null=True,blank=True,max_length=30)
    precio_total8 = models.CharField(null=True,blank=True,max_length=30)
    descripcion8= models.CharField(null=True,blank=True,max_length=30)
    observacion8 = models.TextField(null=True, blank=True)
    
    articulo9 = models.CharField(max_length=30,blank=True)
    cantidad9 = models.CharField(max_length=30,blank=True)
    precio_unitario9 = models.CharField(null=True,blank=True,max_length=30)
    precio_total9 = models.CharField(null=True,blank=True,max_length=30)
    descripcion9= models.CharField(null=True,blank=True,max_length=30)
    observacion9 = models.TextField(null=True, blank=True)
    
    total =   models.CharField(null=True,blank=True,max_length=30)
    
    
    fecha_creacion = models.DateField()
   
    def __str__(self):
            return '{}'.format(self.fecha_creacion)


# Create your models here.

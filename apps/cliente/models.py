from django.db import models
from apps.empresa.models import Empresa_a
from django.contrib import admin
    
 #Modelo de datos de la historia clinica   
# Create your models here.

class Cliente(models.Model):
        
        empresa=models.CharField(max_length = 20)
        nombre = models.CharField(max_length = 20)
        apellidos = models.CharField(max_length = 20)
        Sex=(('M','Masculino'),('F','Femenino'),('O','Otro'))
        sexo = models.CharField(max_length= 1,choices=Sex)
        mail = models.EmailField()
        nit  = models.IntegerField()
        domicilio = models.CharField(max_length=30)
        telefono = models.IntegerField()
        
        
        def __str__(self):
            return '{} {} {}'.format(self.nombre,self.apellidos,self.nit)
   

# Create your models here.

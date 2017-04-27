from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Empresa_a(User):
       
       Sex=(('M','Masculino'),('F','Femenino'),('O','Otro'))
       sexo = models.CharField(max_length= 1,choices=Sex)
       empresa = models.CharField(max_length=50)
       domicilio = models.CharField(max_length=70)
       nit=models.IntegerField()
       Doc = models.IntegerField()
       telefono = models.CharField(max_length=12)
       firma = models.ImageField(upload_to='firma')
       imgperfil = models.ImageField(upload_to='perfil',null=True)
       
       
       def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
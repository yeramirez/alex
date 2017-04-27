from django import forms
from apps.empresa.models import Empresa_a
from django.contrib.auth.forms import UserCreationForm


TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)

class EmpresaForm(UserCreationForm):
    
    class Meta:
        model = Empresa_a
        
        fields =[
            'username',  
            'first_name', 
            'last_name',
            'email',
            'sexo',
            'telefono',
            'password1',
            'password2',
            'telefono',
            'firma',
            'imgperfil',
            'Doc',
            'nit',
            'empresa',
         ]
        
        widgets = {
        
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            'password2':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}), 
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-form-control'},choices=TITLE_SEXO),
            'email':forms.EmailInput(),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'empresa':forms.TextInput(attrs={'class':'form-control'}),
            'Doc':forms.TextInput(attrs={'class':'form-control'}),
            'nit':forms.TextInput(attrs={'class':'form-control'}),
            'firma':forms.FileInput(attrs={'class':'fileupload-new'}),
            'imgperfil':forms.FileInput(attrs={'class':'fileupload-new'}),
        
        }
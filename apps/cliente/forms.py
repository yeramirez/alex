from django import forms
from apps.cliente.models import Cliente


TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)

        
    
class ClienteForm(forms.ModelForm):
    

    class Meta:
        model = Cliente
        
        fields = [
           
            'nombre',
            'apellidos',
            'mail',
            'sexo',
            'empresa',
            'nit',
            'domicilio',
            'telefono',
        ]
        
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(),
            'sexo': forms.Select(attrs={'class':'form-form-control'},choices=TITLE_SEXO),
            'nit': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        }
        
        
                       
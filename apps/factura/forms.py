from django import forms
from apps.factura.models import Factura
from bootstrap3_datetime.widgets import DateTimePicker

TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)

class FacturaForm(forms.ModelForm):
    
    class Meta:
        model = Factura
        
        fields =[
            'fecha_creacion',
            'miempresa',
            'clientes', 
            'articulo',
            'cantidad',
            'precio_unitario',
            'precio_total',
            'descripcion',
            'observacion',
            'total',
            
            'cantidad1',
            'descripcion1',
            'observacion1',
            'precio_unitario1',
            'precio_total1',
               
            'cantidad2',
            'descripcion2',
            'observacion2',
            'precio_unitario2',
            'precio_total2',
            
               
            'cantidad3',
            'descripcion3',
            'observacion3',
            'precio_unitario3',
            'precio_total3',
            
               
            'cantidad4',
            'descripcion4',
            'observacion4',
            'precio_unitario4',
            'precio_total4',
               
            'cantidad5',
            'descripcion5',
            'observacion5',
            'precio_unitario5',
            'precio_total5',
            
               
            'cantidad6',
            'descripcion6',
            'observacion6',
            'precio_unitario6',
            'precio_total6',
               
            'cantidad7',
            'descripcion7',
            'observacion7',
            'precio_unitario7',
            'precio_total7',
            
               
            'cantidad8',
            'descripcion8',
            'observacion8',
            'precio_unitario8',
            'precio_total8',
            
               
            'cantidad9',
            'descripcion9',
            'observacion9',
            'precio_unitario9',
            'precio_total9',
                    
                    
            
           ]
        
        widgets = {
               
            'miempresa': forms.Select(attrs={'class':'form-form-control'}),
            'clientes': forms.Select(attrs={'class':'form-form-control'}),
            'observacion': forms.Textarea(attrs={'class':'form-control'}),
            'fecha_creacion' : forms.TextInput(attrs={'class':'form-control date-picker','data-date-format':'yyyy-mm-dd'}),
            'articulo': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'articulo1': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad1': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion1': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario1': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total1': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'observacion1': forms.Textarea(attrs={'class':'form-control'}),
            'articulo2': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad2': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion2': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario2': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total2': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'observacion2': forms.Textarea(attrs={'class':'form-control'}),
            'articulo3': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad3': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion3': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario3': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total3': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'observacio3': forms.Textarea(attrs={'class':'form-control'}),
            'articulo4': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad4': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion4': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario4': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total4': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'observacion4': forms.Textarea(attrs={'class':'form-control'}),
            'articulo5': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad5': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion5': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario5': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total5': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
             'observacion5': forms.Textarea(attrs={'class':'form-control'}),
            'articulo6': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad6': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion6': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario6': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total6': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
             'observacion6': forms.Textarea(attrs={'class':'form-control'}),
            'articulo7': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad7': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion7': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario7': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total7': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
             'observacion7': forms.Textarea(attrs={'class':'form-control'}),
            'articulo8': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad8': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion8': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario8': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total8': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
             'observacion8': forms.Textarea(attrs={'class':'form-control'}),
            'articulo9': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad9': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion9': forms.TextInput(attrs={'class':'form-control'}),
            'precio_unitario9': forms.TextInput(attrs={'class':'form-control'}),
            'precio_total9': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
             'observacion9': forms.Textarea(attrs={'class':'form-control'}),
            
            
            
            
            'total': forms.TextInput(attrs={'class':'form-control','readonly':"Imc()"}),
            
            
            
        }
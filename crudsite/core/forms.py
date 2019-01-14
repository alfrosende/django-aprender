from django import forms
from .models import Cliente

class CrearForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre','direccion','telefono1','telefono2','tipo_cliente','cedula_identidad','rut']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'telefono1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono2': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_cliente': forms.Select(attrs={'class':'form-control'}),
            'cedula_identidad': forms.NumberInput(attrs={'class':'form-control'}),
            'rut': forms.NumberInput(attrs={'class':'form-control'}),
        }
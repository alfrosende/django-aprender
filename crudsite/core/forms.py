from django import forms
from .models import Cliente
import django_filters

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

class ClientesFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = ['nombre','direccion','tipo_cliente']

    '''
        Para hacer uso de django_filters es necesario pip install django-filters
        En el template para poder modelar se usa widget_tweaks que se instala pip install django-widget-tweaks
    '''
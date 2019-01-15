from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Cliente 
from .forms import CrearForm, ClientesFilter
from django_filters.views import FilterView

'''
    Las vistas basadas en clases tienen varios beneficios como ...
    Documentacion: https://ccbv.co.uk/
'''

class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mivariable'] = "Hola variableeeee"
        return context

class ClientesView_OTRAFORMA_NODARBOLA(FilterView):
    model = Cliente
    context_object_name = 'clientes'
    filterset_class = ClientesFilter
    template_name = "core/cliente_list.html"

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

class ClientesView(ListView):
    '''
     No es necesario el template si se le pone como nombre al mismo nombreModeloMinuscula_list.html
     En el html, para referenciar la variable a iterar se puede hacer con el nombre de variable  nombreModeloMinuscula_list
     u object_list
    '''
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClientesFilter(self.request.GET, queryset=self.get_queryset()) 
        return context
    

class ClienteDetailView(DetailView):
    '''
     Al igual que en el listView no es necesario el template si se le pone como nombre al 
     nombreModeloMinuscula_detail.html
     En el html, para referenciar la variable a iterar se puede hacer con el nombre de variable  nombreModelo
     u object
    '''
    model = Cliente

class CrearClienteView(CreateView):
    # El nombre del template en este caso debe ser nombreModel_form
    model = Cliente
    # Aca le estoy asignando un formulario personalizado por el tema de los estilos
    form_class = CrearForm
    '''
    Elimino esto porque lo tengo en el formulario personalizado
    fields = ['nombre','direccion','telefono1','telefono2','tipo_cliente','cedula_identidad','rut']
    '''
    def get_success_url(self):
        return reverse('clientes') 

class ModificarClienteView(UpdateView):
    model = Cliente
    fields = ['nombre','direccion','telefono1','telefono2','tipo_cliente','cedula_identidad','rut']
    # El sufijo es el nombre que debe llevar el template luego de nombreModelo_
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('clientes') 

class EliminarClienteView(DeleteView):
    model = Cliente
    
    def get_success_url(self):
        return reverse('clientes')
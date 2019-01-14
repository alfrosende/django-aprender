from django.urls import path
from core.views import AboutView, ClientesView, ClienteDetailView, CrearClienteView, ModificarClienteView, EliminarClienteView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', ClientesView.as_view(), name='clientes'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente'),
    path('cliente/crear/', CrearClienteView.as_view(), name='crear_cliente'),
    path('cliente/modificar/<int:pk>', ModificarClienteView.as_view(), name='modificar_cliente'),
    path('cliente/eliminar/<int:pk>', EliminarClienteView.as_view(), name='eliminar_cliente')
]
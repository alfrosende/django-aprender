from django.urls import path
from core import views

urlpatterns = [
    path('', views.vista, name='prueba'),
    path('resp/<int:pk>/', views.respuesta, name='resp'),
]
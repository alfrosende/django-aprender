from django.urls import path
from core.views import ExpedientesView
from . import views

urlpatterns = [
    path('crear/', views.crearView, name='crear'),
    path('', ExpedientesView.as_view(), name='expedientes')
]
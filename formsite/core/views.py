from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Expediente
from .forms import CrearForm

class ExpedientesView(ListView):
    model = Expediente

def crearView(request):
    form = CrearForm()
    return render(request, "core/crear.html", {'form':form})


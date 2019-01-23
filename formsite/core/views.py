from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Expediente, Estado
from .forms import CrearForm
from .persistencia import *
from django.urls import reverse

class ExpedientesView(ListView):
    model = Expediente

def crearView(request):
    form = CrearForm()
    if request.method == 'POST':
        form = CrearForm(data=request.POST)
        if form.is_valid():
            titulo = request.POST.get('titulo', '')
            concepto = request.POST.get('concepto', '')
            estadoid = request.POST.get('estado', '')
            estado = getOneEstado(estadoid)
            
            newexp = creoExpediente(titulo, concepto, estado)
            print("expediente creado = ",newexp.id)
            return redirect(reverse('expedientes')+'?ok')

    return render(request, "core/crear.html", {'form':form})


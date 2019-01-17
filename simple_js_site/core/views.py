from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente  

def vista(request):
    context = {'latest_question_list': 'hola'}
    return render(request,'core/prueba.html', context)

def respuesta(request, pk):
    try:
        micliente = Cliente.objects.get(id=pk)
        json_response = {'verificado': False, 'nombre':micliente.nombre}
    except:
        json_response = {'verificado': False, 'nombre':"nooooo"}
    

    return JsonResponse(json_response)
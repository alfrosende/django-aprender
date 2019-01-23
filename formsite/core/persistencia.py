from .models import *

def getAllEstados():
    return Estado.objects.all()

def getOneEstado(estadoid):
    return Estado.objects.get(id=estadoid)

def creoExpediente(titulo, concepto, estado):
    return Expediente.objects.create(titulo=titulo, concepto=concepto, estado=estado)
from django.contrib import admin
from .models import Cliente, Visita 

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VisitaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Visita, VisitaAdmin)

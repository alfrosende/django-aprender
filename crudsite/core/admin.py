from django.contrib import admin
from .models import Cliente, Visita 

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VisitaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Inyectamos nuestro fichero css para que el ckeditor sea responsivo
    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
            }



admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Visita, VisitaAdmin)

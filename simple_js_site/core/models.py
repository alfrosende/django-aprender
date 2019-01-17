from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
        ordering=['nombre']

    def __str__(self):
        return self.nombre


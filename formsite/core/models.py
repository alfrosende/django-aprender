from django.db import models

class Estado(models.Model):
    abreviada = models.CharField(verbose_name="Abreviada", max_length=3)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=40)

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
        ordering = ["abreviada"]

    def __str__(self):
        return self.descripcion

class Expediente(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=40)
    concepto = models.TextField(verbose_name="Concepto")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "expediente"
        verbose_name_plural = "expedientes"
        ordering = ["estado"]

    def __str__(self):
        return self.titulo
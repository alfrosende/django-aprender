from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Cliente(models.Model):
    PERSONA = 'P'
    EMPRESA = 'E'
    TIPOS_CLIENTE = (
        (PERSONA, 'Persona'),
        (EMPRESA, 'Empresa'),
    )

    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    direccion = models.CharField(verbose_name="Direccion", max_length=200, null=True, blank=True)
    telefono1 = models.CharField(verbose_name="Telefono 1", max_length=20, null=True, blank=True)
    telefono2 = models.CharField(verbose_name="Telefono 2", max_length=20, null=True, blank=True)
    tipo_cliente = models.CharField(verbose_name="Tipo cliente", max_length=1, choices=TIPOS_CLIENTE, default=PERSONA)
    cedula_identidad = models.SmallIntegerField(verbose_name="Cedula identidad", null=True, blank=True)
    rut = models.SmallIntegerField(verbose_name="RUT", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima edicion")
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Visita(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    fecha = models.DateTimeField(verbose_name="Fecha de visita")
    direccion = models.CharField(max_length=200, verbose_name="Direccion")
    notas = RichTextField(verbose_name="Notas")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima edicion")

    class Meta:
        verbose_name = "visita"
        verbose_name_plural = "visitass"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


'''
Todo sobre fields:
    https://docs.djangoproject.com/en/2.1/ref/models/fields/

Parametros de los fields:
    null / blank / choices / default / editable / error_messages / help_text / primary_key /
    unique / verbose_name / validators

Tipos de fileds:
    - BigIntegerField (tipo_html = TextInput) (-9223372036854775808 a 9223372036854775807)  
    - BigIntegerField (tipo_html = TextInput) (-9223372036854775808 a 9223372036854775807)  
    - BooleanField (tipo_html = CheckboxInput o NullBooleanSelect si null=True) (si no se especifica default por defecto viene en Nonre)
    - CharField (tipo_html = TextInput) (obligatorio = max_length)
    - DateField (tipo_html = TextInput) (parametros_utiles = auto_now / auto_now_add)
    - DateTimeField (idem anterior pero con hora)
    - DecimalField (tipo_html = NumberInput) (obligatorio = max_digits / decimal_places)
    - EmailField (tipo_html = TextInput) (obligatorio = max_length)
    - FileField (tipo_html = ??) (parametros_utiles = upload_to)
    - FilePathField (idem anterior pero restringiendo la subida a archivos de un determinado directorio)
    - FloatField (tipo_html = NumberInput) 
    - ImageField (idem FileField pero controla que el archivo subido sea una imagen)
    - IntegerField (tipo_html = NumberInput) (-2147483648 a 2147483647) 
    - GenericIPAddressField (leer documentacion si se necesita)
    - PositiveIntegerField  (idem IntegerField pero solo acepta positivos)
    - PositiveSmallIntegerField (idem SmallIntegerField pero solo acepta positivos)
    - SlugField (es una label corta utilizada para mostrar algo, generalmente se usa para urls o referenciar a un valor calculado a partir de otro campo)
    - SmallIntegerField (tipo_html = NumberInput) (-32768 a 32767)
    - TextField (tipo_html = TextArea) 
    - TimeField (tipo_html = TextInput)
    - URLField (tipo_html = TextInput)

Tipos para relaciones (leer especificaciones de la documentacion):
    - ForeignKey
    - ManyToManyField
    - OneToOneField


CkEditor:
    Para instalar el ckeditor --> pip install ckeditor
    Luego hay que agregarlo en el settings.py en las INSTALED_APPS
    Importar from ckeditor.fields import RichTextField y sustituir el models.TextField por RichTextField
    Finalmente en el template, el template tag que tenia la textarea mostrando el texto enriquecido y debia decir
    |linebreak cambiarlo por |safe, deberia verse asi --> {{page.content|safe}}

    Si se utilizan vistas basadas en clases ...

'''
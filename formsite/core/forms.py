from django import forms
from .models import Expediente, Estado

class CrearForm(forms.Form):
    estados = Estado.objects.all()
    abreviada = forms.CharField(required = True)
    titulo = forms.CharField(required=True)
    concepto = forms.CharField(required=True, widget=forms.Textarea)
    estado = forms.ModelChoiceField(required=True, queryset=estados)


'''
    Los fields pueden tener varios atributos, algunos de ellos son:
        - required --> True o False si el campo es obligatorio o no
        - label --> Nombre del label que va a mostrar el componente
        - initial --> Valor que viene cargado por defecto
        - widget --> Tema importante que tiene muchos usos (ver despues)
        - help_text --> Muestra debajo del componente un texto con lo requerido por el mismo
        - error_messages --> Permite sobreescribir el mensaje de error por defecto
            ej: name = forms.CharField(error_messages={'required': 'Please enter your name'})
        - validators --> Brinda una lista de funciones de validacion para el campo (ver mas adelante)
        - disabled --> True o False si el campo es editable o no

    Tipos de field para formularios:
        - BooleanField --> Widget = CheckboxInput / ErrorMessage = required
        - CharField --> Widget = TextInput / ErrorMessage = required, max_length, min_length / 
                        Validates = max_length, min_length si son preveidos 
        - ChoiceField --> Widget = Select / ErrorMessage = required, invalid_choice / 
                        Validates = que exista el valor en la lista de choices /
                        Argumento extra = choices (lista de elementos a mostrar en el combo)
        - TypedChoiceField --> Todo idem ChoiceField excepto que tiene dos argumentos extra, coerce y empty_value
        - DateField --> Widget = DateInput / ErrorMessage = required, invalid / Validates = Fecha existente / 
                        Argumentos extra = input_formats (lista de formatos aceptados)
                        Por defecto los formatos aceptados son:
                        ['%Y-%m-%d',      # '2006-10-25'
                         '%m/%d/%Y',      # '10/25/2006'
                         '%m/%d/%y']      # '10/25/06'
        - DateTimeField --> Widget = DateTiemInput / ErrorMessage = required, invalid / Validates = Fecha existente / 
                        Argumentos extra = input_formats (lista de formatos aceptados)
                        Por defecto los formatos aceptados son:
                        ['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
                         '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
                         '%Y-%m-%d',             # '2006-10-25'
                         '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
                         '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
                         '%m/%d/%Y',             # '10/25/2006'
                         '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
                         '%m/%d/%y %H:%M',       # '10/25/06 14:30'
                         '%m/%d/%y']             # '10/25/06'
        - DecimalField --> Widget = NumberInput / ErrorMessage = required, invalid, max_value, min_value, max_digits, 
                           max_decimal_places, max_whole_digits / Validates = Que sea un numero / 
                           Argumentos extra = max_value, min_value, max_digits, decimal_places
        - BooleanField --> Widget = TextInput / ErrorMessage = required, invalid / 
                           Validates = que el valor sea un string que se pueda convertir a timedelta 
        - EmailField --> Widget = EmailInput / ErrorMessage = required, invalid
                         Argumentos extra = max_length, min_length
        - FileField --> Widget = ClearableFileInput / ErrorMessage = required, invalid, missing, empty, max_length
        - FilePathField --> Widget = Select / ErrorMessage = required, invalid_choice (ver bien su uso)
        - FloatField --> Widget = NumberInput / ErrorMessage = required, invalid, max_value, min_value /
                         Argumentos extra = max_value, min_value
        - ImageField --> Widget = ClearableFileInput / ErrorMessage = required, invalid, missing, empty, invalid_image /
                         Validate = que la seleccion sea un formato de imagen reconocido por Pillow
        - IntegerField --> Widget = NumberInput / ErrorMessage = required, invalid, max_value, min_value /
                           Argumentos extra = max_value, min_value
        - GenericIPAddressField --> Widget = TextInput / ErrorMessage = required, invalid / Validate = Ip valida /
                                    Argumentos extra = protocol, unpack_ipv4
        - MultipleChoiceField --> Widget = SelectMultiple / ErrorMessage = required, invalid_choice, invalid_list /
                                  Argumento extra = choices (lista de elementos a mostrar en el combo)
        - ModelChoiceField --> Widget = Select / ErrorMessage = required, invalid_choice /
                               Argumentos extra = queryset, empty_label
        Hay algunos mas pero me aburri
'''
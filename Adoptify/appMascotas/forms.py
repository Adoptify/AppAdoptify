from django.forms import ModelForm, Form, ChoiceField
from appMascotas.models import *


class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['descripcion', 'telefono', 'localidad',
                  'especie', 'raza', 'edad', 'sexo', 'foto']


class FiltrarPublicacion(Form):
    # Ya que quiero un campo que sea sin valor(None), en el parametro choices
    # empiezo creando dos listas, una con una tupla vacia, y otra con tuplas que
    # representan a cada objeto de la tabla que estoy trayendo, por ultimo
    # tomo ambas listas, las fusiono y convierto en una tupla
    localidad = ChoiceField(label='Localidad:', choices=tuple(
        [(None, 'Seleccione')] + [(l.id, l.nombre) for l in Localidad.objects.all()]), required=False)
    edad = ChoiceField(label='Edad:', choices=tuple(
        [(None, 'Seleccione')] + [(e.id, e.edad) for e in Edad.objects.all()]), required=False)
    sexo = ChoiceField(label='Sexo:', choices=tuple(
        [(None, 'Seleccione')] + [(s.id, s.nombre) for s in Sexo.objects.all()]), required=False)
    raza = ChoiceField(label='Raza:', choices=tuple(
        [(None, 'Seleccione')] + [(r.id, r.nombre) for r in Raza.objects.all()]), required=False)
    especie = ChoiceField(label='Especie:', choices=tuple(
        [(None, 'Seleccione')] + [(esp.id, esp.nombre) for esp in Especie.objects.all()]), required=False)

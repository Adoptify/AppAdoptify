from django.forms import ModelForm
from appMascotas.models import Publicacion


class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['descripcion', 'telefono', 'localidad',
                  'especie', 'raza', 'edad', 'sexo', 'foto']

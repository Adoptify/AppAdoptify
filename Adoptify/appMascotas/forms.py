from django.forms import ModelForm, Form, ChoiceField
from django import forms
from appMascotas.models import *


class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ['telefono', 'localidad',
                  'especie', 'raza', 'edad', 'sexo', 'descripcion', 'foto']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control descripcion', 'rows': '7'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'raza': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'})
        }


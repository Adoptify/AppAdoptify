from django.shortcuts import render, redirect
from appMascotas.models import Publicacion
from appMascotas.forms import *
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
# Create your views here.


def index(request, pubsFiltradas=None):
    form = FiltrarPublicacion()
    if pubsFiltradas != None:
        filtro = pubsFiltradas
    else:
        filtro = Publicacion.objects.all()
    Q1 = Q(report__lt=3)
    Q2 = Q(fechavence__gt=datetime.now())
    publicaciones = filtro.filter(Q1 & Q2)
    paginator = Paginator(publicaciones, 3)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)
    return render(request, 'index2.html', {'publicaciones': publicaciones, 'form': form})


def crear(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PublicacionForm()
        return render(request, 'nuevPu.html', {'form': form})


def publicacion(request, id):
    try:
        publicacion = Publicacion.objects.get(pk=id)
    except Publicacion.DoesNotExist:
        raise Http404("La cuenta no existe")

    return render(request,
                  'publicacion.html',
                  {'publicacion': publicacion})


def filtrarPublicacion(request):
    if request.method == 'POST':
        form = FiltrarPublicacion(request.POST)
        if form.is_valid():
            localidad = form.cleaned_data['localidad']
            edad = form.cleaned_data['edad']
            raza = form.cleaned_data['raza']
            sexo = form.cleaned_data['sexo']
            especie = form.cleaned_data['especie']
            return index(request, Publicacion.filtrar(localidad, edad, especie, raza, sexo))


def reportar(request, pk):

    if request.method == 'POST':
        p = Publicacion.objects.get(id=pk)
        p.report = p.report+1
        p.save()
        return redirect(f'/{p.id}')

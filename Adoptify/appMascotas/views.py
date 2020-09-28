from django.shortcuts import render, redirect
from appMascotas.models import *
from appMascotas.forms import PublicacionForm
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    filtro = Publicacion.objects.all()
    Qe = Q()
    if request.POST.get('edadget'):
        edad = int(request.POST.get('edadget'))
        Qe = Q(edad=edad)
    Q1 = Q(report__lt=3)
    Q2 = Q(fechavence__gt=datetime.now())
    publicaciones = filtro.filter(Q1 & Q2 & Qe)
    paginator = Paginator(publicaciones, 3)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)
    context = {'publicaciones': publicaciones, 'edades': Edad.objects.all()}
    return render(request, 'appMascotas/index.html', context)


def crear(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PublicacionForm()
        context = {'form': form}
        return render(request, 'appMascotas/nuevPu.html', context)


def publicacion(request, id):
    try:
        publicacion = Publicacion.objects.get(pk=id)
    except Publicacion.DoesNotExist:
        raise Http404("La cuenta no existe")
    context = {'publicacion': publicacion}
    return render(request,
                  'appMascotas/publicacion.html',
                  context)


def reportar(request, pk):
    if request.method == 'POST':
        p = Publicacion.objects.get(id=pk)
        p.report = p.report+1
        p.save()
        return redirect(f'/{p.id}')

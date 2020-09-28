from django.shortcuts import render, redirect
from appMascotas.models import *
from appMascotas.forms import PublicacionForm
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    allPubs = Publicacion.objects.all()
    Qe = Q()
    Ql = Q()
    Qs = Q()
    Qes = Q()
    Qr = Q()
    if request.POST.get('edadget'):
        edad = (request.POST.get('edadget'))
        Qe = Q(edad__edad=edad)
    if request.POST.get('localidadget'):
        localidad = (request.POST.get('localidadget'))
        Ql = Q(localidad__nombre=localidad)
    if request.POST.get('sexoget'):
        sexo = (request.POST.get('sexoget'))
        Qs = Q(sexo__nombre=sexo)
    if request.POST.get('especieget'):
        especie = (request.POST.get('especieget'))
        Qes = Q(especie__nombre=especie)
    if request.POST.get('razaget'):
        raza = (request.POST.get('razaget'))
        Qr = Q(raza__nombre=raza)
    Q1 = Q(report__lt=3)
    Q2 = Q(fechavence__gt=datetime.now())
    pubsFiltradas = allPubs.filter(Q1 & Q2 & Qe & Ql & Qs & Qes & Qr)
    cantPaginacion = 3
    paginator = Paginator(pubsFiltradas, cantPaginacion)
    page = request.GET.get('page')
    pagActual = paginator.get_page(page)
    # total de resultados obtenidos en la bd
    total = len(allPubs)
    contResActual = 0
    for pagina in range(1, pagActual.number+1):
        contResActual += cantPaginacion

    contResActual -= cantPaginacion-1
    totalActual = cantPaginacion * pagActual.number if cantPaginacion * \
        pagActual.number < total else total
    context = {
        'publicaciones': pagActual,
        'edades': Edad.objects.all(),
        'localidades': Localidad.objects.all(),
        'sexos': Sexo.objects.all(),
        'razas': Raza.objects.all(),
        'especies': Especie.objects.all(),
        'totalActual': totalActual,
        'total': total,
        'cantPaginacion': cantPaginacion,
        'contResActual': contResActual
    }
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

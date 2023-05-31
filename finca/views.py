from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Productor
from finca.models import Finca, Recolector, Recoleccion
# Create your views here.


def agregar(request,pk):

    if request.method == 'POST':
        
        # datos finca 
        nombref = request.POST.get('nombref')
        telefonof = request.POST.get('telefonof')
        direccionf = request.POST.get('direccionf')
        
        miProductor=Productor.objects.get(pk=pk)

        Finca.objects.create(
            nombre = nombref,
            direccion = direccionf,
            telefono = telefonof,
            productor = miProductor
        )

        messages.success(request, 'Finca Registrada Correctamente')
        return redirect('fincas',pk)

    miProductor=Productor.objects.get(pk=pk)
    
    return render(request, 'finca/agregar.html', {
        'title': 'Agregar Finca',
        'productor': miProductor
    })

def mostrar(request, pk):
    fincas = Finca.objects.filter(productor=pk)
    productor = Productor.objects.get(pk=pk)
    
    return render(request, 'finca/mostrar.html', {
        'title': 'Lista Fincas',
        'fincas': fincas,
        'productor': productor,
    })

def editar(request, pk):

    if request.method == 'POST':
        #datos productor
        nombref = request.POST.get('nombref')
        telefonof = request.POST.get('telefonof')
        direccionf = request.POST.get('direccionf')
        productor = request.POST.get('productorf')

        miProductor=Productor.objects.get(pk=productor) #pendiente

        finca = Finca.objects.filter(
            pk=pk
        ).update(
            nombre = nombref,
            direccion = direccionf,
            telefono = telefonof,
            productor = miProductor
        )

        messages.success(request, 'Actualizado Correctamente')
        return redirect('fincas', productor)

    finca = Finca.objects.get(pk=pk)
    # productor = Productor.objects.get(nombres=finca.productor)
    productores = Productor.objects.all()

    return render(request, 'finca/editar.html', {
        'title': 'Ver Finca',
        'finca': finca,
        'productores': productores
    })

def eliminar(request, pk):
    finca = get_object_or_404(Finca, pk=pk)
    finca.delete()
    messages.success(request, 'Borrado Correctamente')

def agregarRecoleccion(request, pk):

    if request.method == 'POST':
        # datos recoleccion 
        fincaf = request.POST.get('fincaf')
        recolectorf = request.POST.get('recolectorf')
        cantidadf = request.POST.get('cantidadf')
        novedadf = request.POST.get('novedadf')

        miFinca = Finca.objects.get(pk = fincaf)
        miProductor = Productor.objects.get(pk = miFinca.productor.pk)

        Recoleccion.objects.create(
            productor = miProductor,
            recolector = Recolector.objects.get(pk=recolectorf),
            finca = miFinca,
            cantidad = cantidadf,
            novedad = novedadf
        )

        messages.success(request, 'Recoleccion Completada')
        return redirect('fincas', miProductor.pk)

    finca = Finca.objects.get(pk=pk)
    fincas = Finca.objects.filter(productor=finca.productor)
    recolectores = Recolector.objects.all()
    
    return render(request, 'recoleccion/agregar.html', {
        'title': 'Agregar Finca',
        'fincaE': finca,
        'fincas':fincas,
        'recolectores':recolectores
    })

def mostrarRecoleccion(request, pk):

    finca = Finca.objects.get(pk=pk)
    recolecciones = Recoleccion.objects.filter(finca=finca)
    
    return render(request, 'recoleccion/mostrar.html', {
        'title': 'Agregar Finca',
        'fincaE': finca,
        'recolecciones':recolecciones
    })
    
def recibos(request,pk):
    finca = Finca.objects.get(pk=pk)
    litros = Recoleccion.objects.filter(finca=finca)
    
    return render(request, 'recoleccion/editar.html', {
        'title': 'Facturas de Pedidos',
        'fincaE': finca,
        'litros':litros,
    })


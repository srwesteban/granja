from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Productor
from finca.models import Finca
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
        return redirect('/')

    return render(request, 'finca/agregar.html', {
        'title': 'Agregar Finca'
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
        return redirect('/')

    finca = Finca.objects.get(pk=pk)

    return render(request, 'finca/editar.html', {
        'title': 'Ver Finca',
        'finca': finca
    })

def eliminar(request, pk):
    finca = get_object_or_404(Finca, pk=pk)
    finca.delete()
    messages.success(request, 'Borrado Correctamente')

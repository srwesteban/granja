from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Recolector
from finca.models import Finca
# Create your views here.


def agregar(request):

    if request.method == 'POST':
        #datos recolector
        nombres = request.POST.get('nombre')
        apellidos = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        fNacimiento = request.POST.get('fnacimiento')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        # datos finca 
        nombref = request.POST.get('nombref')
        telefonof = request.POST.get('telefonof')
        direccionf = request.POST.get('direccionf')
        
        miRecolector = Recolector.objects.create(
            cedula = cedula,
            nombres = nombres,
            apellidos = apellidos,
            direccion = direccion,
            fNacimiento = fNacimiento,
            telefono = telefono
        )

        messages.success(request, 'Registrado Correctamente')
        return redirect('/')

    return render(request, 'recolector/agregar.html', {
        'title': 'Agregar Recolector'
    })

def mostrar(request):
    recolectores = Recolector.objects.all()
    return render(request, 'recolector/mostrar.html', {
        'title': 'Lista Recolectores',
        'recolectores': recolectores
    })

def editar(request, pk):

    if request.method == 'POST':
        #datos recolector
        nombres = request.POST.get('nombre')
        apellidos = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        fNacimiento = request.POST.get('fnacimiento')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        recolector = Recolector.objects.filter(
            pk=pk
        ).update(
            cedula = cedula,
            nombres = nombres,
            apellidos = apellidos,
            direccion = direccion,
            fNacimiento = fNacimiento,
            telefono = telefono
        )

        messages.success(request, 'Actualizado Correctamente')
        return redirect('/')

    recolector = Recolector.objects.get(pk=pk)

    return render(request, 'recolector/editar.html', {
        'title': 'Ver recolector',
        'recolector': recolector
    })

def eliminar(request, pk):
    recolector = get_object_or_404(Recolector, pk=pk)
    recolector.delete()
    messages.success(request, 'Borrado Correctamente')

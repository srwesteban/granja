from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Productor
from finca.models import Finca
# Create your views here.


def agregar(request):

    if request.method == 'POST':
        #datos productor
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
        
        miProductor = Productor.objects.create(
            cedula = cedula,
            nombres = nombres,
            apellidos = apellidos,
            direccion = direccion,
            fNacimiento = fNacimiento,
            telefono = telefono
        )

        miFinca = Finca.objects.create(
            nombre = nombref,
            direccion = direccionf,
            telefono = telefonof,
            productor = miProductor
        )

        messages.success(request, 'Registrado Correctamente')
        return redirect('/')

    return render(request, 'productor/agregar.html', {
        'title': 'Agregar Productor'
    })

def mostrar(request):
    productores = Productor.objects.all()
    return render(request, 'productor/mostrar.html', {
        'title': 'Lista Productores',
        'productores': productores
    })

def editar(request, pk):

    if request.method == 'POST':
        #datos productor
        nombres = request.POST.get('nombre')
        apellidos = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        fNacimiento = request.POST.get('fnacimiento')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        productor = Productor.objects.filter(
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

    productor = Productor.objects.get(pk=pk)

    return render(request, 'productor/editar.html', {
        'title': 'Ver Productor',
        'productor': productor
    })

def eliminar(request, pk):
    productor = get_object_or_404(Productor, pk=pk)
    productor.delete()
    messages.success(request, 'Borrado Correctamente')

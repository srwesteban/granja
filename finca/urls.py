from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.mostrar, name="fincas"),
    path('add/<int:pk>', views.agregar, name="agregarfinca"),
    path('view/<int:pk>', views.editar, name="verfinca"),
    path('delete/<int:pk>', views.eliminar, name="eliminarfinca"),
    path('recoleccion/add/<int:pk>', views.agregarRecoleccion, name="agregarrecoleccion"),
    path('recoleccion/view/<int:pk>', views.mostrarRecoleccion, name="verrecoleccion"),
    path('recoleccion/sale/<int:pk>', views.recibos, name="recibosrecoleccion"),
    path('recoleccion/delete/<int:pk>', views.recibos, name="eliminarrecoleccion")

]

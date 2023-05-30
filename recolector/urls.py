from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar, name="recolectores"),
    path('add', views.agregar, name="agregarrecolector"),
    path('view/<int:pk>', views.editar, name="verrecolector"),
    path('delete/<int:pk>', views.eliminar, name="eliminarrecolector"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar, name="productores"),
    path('add', views.agregar, name="agregarproductor"),
    path('view/<int:pk>', views.editar, name="verproductor"),
    path('delete/<int:pk>', views.eliminar, name="eliminarproducto"),
]

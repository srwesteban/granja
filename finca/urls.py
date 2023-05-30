from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.mostrar, name="fincas"),
    path('add/<int:pk>', views.agregar, name="agregarfinca"),
    path('view/<int:pk>', views.editar, name="verfinca"),
    path('delete/<int:pk>', views.eliminar, name="eliminarfinca"),
]

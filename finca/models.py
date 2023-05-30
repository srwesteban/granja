from django.db import models
from productor.models import Productor
from recolector.models import Recolector
# Create your models here.

class Finca(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre Finca')
    direccion = models.CharField(max_length=150, verbose_name='Direccion Finca')
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name="Teléfono")
    productor = models.ForeignKey(Productor, null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Finca'
        verbose_name_plural = 'Fincas'

    def __str__(self):
        return str(self.cedula)

class Recoleccion(models.Model):
    productor = models.ForeignKey(Productor, null=True, blank=True, on_delete=models.CASCADE)
    recolector = models.ForeignKey(Recolector, null=True, blank=True, on_delete=models.CASCADE)
    finca = models.ForeignKey(Finca, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Cantidad de leche')
    novedad = models.CharField(max_length=250, null=True, blank=True, verbose_name='novedad')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Recoleccion'
        verbose_name_plural = 'Recolecciones'

    def __str__(self):
        return str(self.productor)
    
    def precioLitro(self):
        return self.cantidad*7000
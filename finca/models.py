from django.db import models
from productor.models import Productor
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

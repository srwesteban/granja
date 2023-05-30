from django.db import models

# Create your models here.

class Recolector(models.Model):
    cedula = models.CharField(max_length=40, unique=True, verbose_name='Cedula')
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')
    fNacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de cumpleaños")
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name="Teléfono")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Recolector'
        verbose_name_plural = 'Recolectores'

    def __str__(self):
        return str(self.cedula)
    
    def calcular_edad(self):
        return date.today().year - self.fNacimiento.year
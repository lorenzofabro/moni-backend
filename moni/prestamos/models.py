from django.db import models
from django.db.models.base import Model

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    key = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'generos'

class PedidoPrestamo(models.Model):
    dni = models.IntegerField(null=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)
    monto = models.IntegerField()
    aprobado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'DNI: {self.dni} - Monto: {self.monto} - Aprobado: {self.aprobado}'

    class Meta:
        db_table = 'pedidos_prestamo'
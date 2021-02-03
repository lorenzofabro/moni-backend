import math
from rest_framework import serializers
from .models import PedidoPrestamo

class PedidoPrestamoSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if math.isnan(attrs['dni']) or attrs['dni'] < 0:
            raise serializers.ValidationError('El DNI no tiene un formato correcto')

        if math.isnan(attrs['monto']) or attrs['monto'] < 0:
            raise serializers.ValidationError('El monto no tiene un formato correcto') 
        return attrs
    
    class Meta:
        model = PedidoPrestamo
        fields = ['id', 'dni', 'nombre', 'apellido', 'genero', 'email', 'monto', 'aprobado']
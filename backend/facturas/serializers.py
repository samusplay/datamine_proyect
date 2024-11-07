# backend/facturas/serializers.py

from rest_framework import serializers
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['numero_contador', 'contador_mes_actual', 'usuario']  # Campos esenciales que recibirá y enviará el frontend

    # Validación para asegurar que 'contador_mes_actual' sea un entero y esté en el formato adecuado
    def validate_contador_mes_actual(self, value):
        try:
            return int(value)
        except ValueError:
            raise serializers.ValidationError("El valor de contador_mes_actual debe ser un número entero.")

    # Método para calcular y devolver los campos adicionales que el backend procesará
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Agregar el campo 'consumo' y 'costo_total' calculado desde el backend
        representation['consumo'] = instance.consumo
        representation['costo_total'] = instance.costo_total
        return representation



# backend/facturas/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Factura
from .serializers import FacturaSerializer

class FacturaListCreateView(ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def create(self, request, *args, **kwargs):
        # Obtener datos del request
        numero_contador = request.data.get("numero_contador")
        try:
            contador_mes_actual = int(request.data.get("contador_mes_actual"))
        except (TypeError, ValueError):
            return Response(
                {"error": "El valor de 'contador_mes_actual' debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verificar duplicados
        if Factura.objects.filter(numero_contador=numero_contador, contador_mes_actual=contador_mes_actual).exists():
            return Response(
                {"error": "Ya existe una factura para este contador en el mes actual."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Obtener el contador del mes anterior si existe
        ultima_factura = Factura.objects.filter(numero_contador=numero_contador).order_by('-contador_mes_actual').first()
        contador_mes_anterior = ultima_factura.contador_mes_actual if ultima_factura else 0

        # Validación: El contador de mes actual debe ser mayor al contador de mes anterior
        if contador_mes_actual <= contador_mes_anterior:
            return Response(
                {"error": "El contador del mes actual debe ser mayor que el contador del mes anterior."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Calcular el consumo total
        consumo_total = contador_mes_actual - contador_mes_anterior

        # Calcular el consumo promedio en kWh por hora (asumiendo 720 horas en el mes)
        consumo_kwh_por_hora = consumo_total / 720

        # Calcular el costo total en pesos colombianos
        tarifa_kwh = 0.15  # Tarifa en dólares por kWh
        tasa_cambio = 4000  # Tasa de cambio de USD a COP
        costo_total_cop = consumo_total * tarifa_kwh * tasa_cambio

        # Preparar los datos para guardar
        data = request.data.copy()
        data['contador_mes_anterior'] = contador_mes_anterior
        data['consumo'] = consumo_total
        data['consumo_kwh_por_hora'] = consumo_kwh_por_hora
        data['costo_total'] = costo_total_cop

        # Serializar y guardar la factura
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Devolver los datos calculados
        return Response(serializer.data, status=status.HTTP_201_CREATED)







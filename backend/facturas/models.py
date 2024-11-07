# backend/facturas/models.py


from django.db import models
from django.contrib.auth import get_user_model

class Factura(models.Model):
    numero_contador = models.CharField(max_length=20)
    contador_mes_anterior = models.IntegerField(null=True, blank=True)
    contador_mes_actual = models.IntegerField()
    consumo = models.IntegerField(null=True, blank=True)
    consumo_kwh_por_hora = models.FloatField(null=True, blank=True)  # Nuevo campo opcional
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    costo_total_cop = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # Nuevo campo opcional
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)

    # Métodos para cálculos se manejarán en la vista


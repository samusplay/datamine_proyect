from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_pago, name='registrar_pago'),
    path('detalle/<int:id>/', views.detalle_pago, name='detalle_pago'),
    path('', views.listar_pagos, name='listar_pagos'),
]

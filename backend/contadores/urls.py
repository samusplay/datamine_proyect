from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_consumo, name='registrar_consumo'),
    path('detalle/<int:id>/', views.detalle_contador, name='detalle_contador'),
    path('', views.listar_contadores, name='listar_contadores'),
]

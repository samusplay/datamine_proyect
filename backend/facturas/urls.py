from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_factura, name='crear_factura'),
    path('detalle/<int:id>/', views.detalle_factura, name='detalle_factura'),
    path('', views.listar_facturas, name='listar_facturas'),
]

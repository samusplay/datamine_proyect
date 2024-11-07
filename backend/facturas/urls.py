from django.urls import path
from .views import FacturaListCreateView

urlpatterns = [
    path('', FacturaListCreateView.as_view(), name='factura-list-create'),
]

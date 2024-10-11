from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductoListCreateView, ejemplo

# Mediciones de Energia
router = DefaultRouter()
router.register('mediciones', ProductoListCreateView)

urlpatterns = [
    # Ruta de prueba para ver que todo funcione
    path('consumo/', ejemplo, name='consumo'),
    
    # Rutas de las API registradas en el router
    path('', include(router.urls)),
]


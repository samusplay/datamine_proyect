from django.urls import path, include

urlpatterns = [
    path('usuarios/', include('backend.usuarios.urls')),  # Incluimos las rutas de usuarios
]






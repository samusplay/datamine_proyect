from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

# Vista que maneja el CRUD de usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()  # Obtiene todos los usuarios de la base de datos
    serializer_class = UsuarioSerializer  # Utiliza el serializer que creamos para los usuarios


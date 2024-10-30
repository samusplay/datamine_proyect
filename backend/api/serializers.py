from rest_framework import serializers
from usuarios.models import Usuario

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'
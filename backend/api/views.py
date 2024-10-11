from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,viewsets
from .models import Producto
from .serializers import ProductoSerializer


def ejemplo(request):
    data={
        'mensaje':'Bienvenido a la API de consumo energetico'
    }
    return JsonResponse(data)

# Create your views here.

class ProductoListCreateView(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer


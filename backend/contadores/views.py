from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registrar_consumo(request):
    return HttpResponse("Consumo registrado")

def detalle_contador(request,id):
    return HttpResponse(f"Detalle del contador con ID {id}")

def listar_contadores(request):
    return HttpResponse("Lista de contadores")
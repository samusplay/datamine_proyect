from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def crear_factura(request):
    return HttpResponse("Factura creada")

def detalle_factura(request,id):
    return HttpResponse(f"Detalle de la factura con ID {id}")

def listar_facturas(request):
    return HttpResponse("lista de facturas")
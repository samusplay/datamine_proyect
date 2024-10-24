from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registrar_pago(request):
    return HttpResponse("Pago registrado")

def detalle_pago(request,id):
    return HttpResponse(f"Detalle del pago con ID {id}")

def listar_pagos(request):
    return HttpResponse("Lista de pagos")
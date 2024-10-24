from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def crear_usuario(request):
    return HttpResponse("Usuario Creado")

def editar_usuario(request,id):
    return HttpResponse(f"Editar usuario con ID {id}")

def eliminar_usuario(request,id):
    return HttpResponse(f"Eliminar usurio con ID {id}")

def listar_usuarios(request):
    return HttpResponse("Lista de usuarios")
from django.shortcuts import render
from django.http import JsonResponse

def ejemplo(request):
    data={
        'mensaje':'!Hola desde la Api'
    }
    return JsonResponse(data)

# Create your views here.

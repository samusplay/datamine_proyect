from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns=[
    path('register/',views.register, name='register'),
]

def register(request):
    return HttpResponse("Pagina de registro de usuarios")
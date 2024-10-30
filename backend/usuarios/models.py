from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del usuario
    tipoUsuario = models.CharField(max_length=50, choices=[('Inquilino', 'Inquilino'), ('Dueño', 'Dueño')])  # Tipo de usuario
    numeroContador = models.CharField(max_length=50)  # Número de contador

    def __str__(self):
        return f'{self.nombre} ({self.tipoUsuario})'
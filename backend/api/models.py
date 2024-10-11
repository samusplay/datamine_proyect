from django.db import models

class Producto(models.Model):
    nombre=models.CharField(max_length=225)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    descripcion=models.TextField()

    def __str__(self):
        return self.nombre


# Create your models here.

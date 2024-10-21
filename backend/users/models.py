from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    # Cambiamos el related_name para evitar el conflicto con el modelo auth.User
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Cambia el nombre de la relación inversa
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Cambia el nombre de la relación inversa
        blank=True
    )
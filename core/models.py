from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    telefono = models.SmallIntegerField(null=True)
    codigo_postal = models.SmallIntegerField(null=True)
    pais = models.CharField(max_length=30, null=True)
    estado = models.CharField(max_length=30, null=True)
    municipio = models.CharField(max_length=30, null=True)
    localidad = models.CharField(max_length=30, null=True)
    colonia = models.CharField(max_length=30, null=True)
    calle = models.CharField(max_length=30, null=True)
    
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from categorias.models import Categorias
from tiendas.models import Tiendas

# Utilities
from utils.models import CRideModel


class Productos(CRideModel):
    objects=models.Manager()
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE,)
    tienda = models.ForeignKey(Tiendas,on_delete=models.CASCADE,)
    
    def __str__(self):
        """Return username."""
        return self.nombre

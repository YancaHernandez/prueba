from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from utils.models import CRideModel

class Categorias(CRideModel):
    objects=models.Manager()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

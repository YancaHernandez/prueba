from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from utils.models import CRideModel

from users.models import User

class Tiendas(CRideModel):
    objects=models.Manager()
    nombre = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """Return username."""
        return self.nombre

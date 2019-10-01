from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from productos.models import Productos
from users.models import User

# Utilities
from utils.models import CRideModel

class Compras(CRideModel):
    objects=models.Manager()
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
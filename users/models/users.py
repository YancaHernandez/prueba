"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from utils.models import CRideModel

class User(CRideModel, AbstractUser):
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']


    is_cliente = models.BooleanField(default=True)
    is_administrador = models.BooleanField(default=False)

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
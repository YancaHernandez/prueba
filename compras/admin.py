from django.contrib import admin
from .models import Compras

class CompraAdmin(Compras):
    list_display = ('nombre')

# admin.site.register(Compras, CompraAdmin)
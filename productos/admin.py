from django.contrib import admin
from productos.models import Productos

class ProductoAdmin(Productos):
    list_display = ('nombre')

# admin.site.register(Productos, ProductoAdmin)
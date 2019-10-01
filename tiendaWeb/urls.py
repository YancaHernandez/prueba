
from django.contrib import admin
from django.urls import include,path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('categorias.urls')),
    path('productos/', include('productos.urls')),
    path('compras/', include('compras.urls')),
    path('', include(('users.urls', 'users'), namespace='users')),
]

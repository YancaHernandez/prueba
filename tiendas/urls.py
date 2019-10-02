from django.urls import include, path

from tiendas import views

# app_name = 'estudiantes'
urlpatterns = [
    path('', views.tiendas_list,name="tiendas"),
    path('<int:pk>/', views.tiendas_detail,name="tiendas_id"),
]

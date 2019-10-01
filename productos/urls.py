from django.urls import include, path

from productos import views

# app_name = 'estudiantes'
urlpatterns = [
    path('', views.productos_list,name="productos"),
    path('<int:pk>/', views.productos_detail,name="productos_id"),
]

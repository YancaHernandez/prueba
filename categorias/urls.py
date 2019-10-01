from django.urls import include, path

from categorias import views

# app_name = 'estudiantes'
urlpatterns = [
    path('', views.categorias_list,name="categorias"),
    path('<int:pk>/', views.categorias_detail,name="categorias_id"),
]

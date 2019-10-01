from django.urls import include, path

from compras import views

urlpatterns = [
    path('', views.compras_list,name="compras"),
    path('<int:pk>/', views.compras_detail,name="compras_id"),
]

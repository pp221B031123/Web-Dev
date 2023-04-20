from django.urls import path, re_path
from api import views

urlpatterns = [
    path('home/', views.home),
    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_details),
    path("categories/", views.category_list),
    path('categories/<int:category_id>/', views.category_details),
    path('categories/<int:category_id>/products/', views.category_product_list),
]
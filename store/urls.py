from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>', views.product_detail, name='product_list')
]
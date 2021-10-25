from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    path('hello/', views.product_list, name='product_list')
]
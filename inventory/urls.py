from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreate.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', views.CategoryUpdate.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/add/', views.ProductCreate.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', views.ProductUpdate.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
]
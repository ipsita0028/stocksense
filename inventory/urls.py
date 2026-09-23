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
    path('stock/add/', views.StockEntryCreate.as_view(), name='stock_add'),
    path('customers/', views.CustomerList.as_view(), name='customer_list'),
    path('customers/add/', views.CustomerCreate.as_view(), name='customer_add'),
    path('customers/<int:pk>/edit/', views.CustomerUpdate.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer_delete'),
    path('bills/', views.BillList.as_view(), name='bill_list'),
    path('bills/new/', views.BillCreate.as_view(), name='bill_add'),
    path('bills/<int:pk>/', views.BillDetail.as_view(), name='bill_detail'),
    path('bills/<int:bill_id>/add-item/', views.BillItemCreate.as_view(), name='billitem_add'),
]
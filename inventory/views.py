from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Category, Product


class CategoryMixin(LoginRequiredMixin):
    model = Category
    success_url = reverse_lazy('category_list')


class CategoryForm(CategoryMixin):
    fields = ['name']
    template_name = 'auth.html'


class CategoryList(CategoryMixin, ListView):
    pass


class CategoryCreate(CategoryForm, CreateView):
    extra_context = {'title': 'Add Category'}


class CategoryUpdate(CategoryForm, UpdateView):
    extra_context = {'title': 'Edit Category'}


class CategoryDelete(CategoryMixin, DeleteView):
    pass


class ProductMixin(LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('product_list')


class ProductForm(ProductMixin):
    fields = ['name', 'category', 'cost_price', 'selling_price', 'stock', 'reorder_level']
    template_name = 'auth.html'


class ProductList(ProductMixin, ListView):
    pass


class ProductCreate(ProductForm, CreateView):
    extra_context = {'title': 'Add Product'}


class ProductUpdate(ProductForm, UpdateView):
    extra_context = {'title': 'Edit Product'}


class ProductDelete(ProductMixin, DeleteView):
    pass
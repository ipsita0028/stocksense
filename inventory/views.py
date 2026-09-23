from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Category, Product, StockEntry, Customer , Bill, BillItem
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


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
    def get_queryset(self):
        qs = super().get_queryset().select_related('category')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('category')
        if q:
            qs = qs.filter(name__icontains=q)
        if cat:
            qs = qs.filter(category_id=cat)
        return qs

    def get_context_data(self, **kwargs):
        return super().get_context_data(categories=Category.objects.all(), **kwargs)
    


class ProductCreate(ProductForm, CreateView):
    extra_context = {'title': 'Add Product'}


class ProductUpdate(ProductForm, UpdateView):
    extra_context = {'title': 'Edit Product'}


class ProductDelete(ProductMixin, DeleteView):
    pass

class StockEntryCreate(LoginRequiredMixin, CreateView):
    model = StockEntry
    fields = ['product', 'quantity']
    template_name = 'auth.html'
    extra_context = {'title': 'Add Stock'}
    success_url = reverse_lazy('product_list')
class CustomerMixin(LoginRequiredMixin):
    model = Customer
    success_url = reverse_lazy('customer_list')


class CustomerForm(CustomerMixin):
    fields = ['name', 'phone', 'credit_limit']
    template_name = 'auth.html'


class CustomerList(CustomerMixin, ListView):
    pass


class CustomerCreate(CustomerForm, CreateView):
    extra_context = {'title': 'Add Customer'}


class CustomerUpdate(CustomerForm, UpdateView):
    extra_context = {'title': 'Edit Customer'}


class CustomerDelete(CustomerMixin, DeleteView):
    pass

class BillCreate(LoginRequiredMixin, CreateView):
    model = Bill
    fields = ['customer', 'payment_type']
    template_name = 'auth.html'
    extra_context = {'title': 'New Bill'}

    def get_success_url(self):
        return reverse_lazy('bill_detail', args=[self.object.pk])


class BillDetail(LoginRequiredMixin, generic.DetailView):
    model = Bill


class BillItemCreate(LoginRequiredMixin, CreateView):
    model = BillItem
    fields = ['product', 'quantity', 'price']
    template_name = 'auth.html'
    extra_context = {'title': 'Add Item'}

    def form_valid(self, form):
        form.instance.bill_id = self.kwargs['bill_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bill_detail', args=[self.kwargs['bill_id']])


class BillList(LoginRequiredMixin, ListView):
    model = Bill
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.db.models import F
from django.shortcuts import render, redirect

from .forms import RegisterForm
from inventory.models import Product


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.groups.add(Group.objects.get(name='Staff'))
        login(request, user)
        messages.success(request, 'Welcome to StockSense!')
        return redirect('home')
    return render(request, 'auth.html', {'form': form, 'title': 'Register'})


def home(request):
    low_stock = Product.objects.filter(stock__lte=F('reorder_level')) if request.user.is_authenticated else []
    return render(request, 'home.html', {'low_stock': low_stock})
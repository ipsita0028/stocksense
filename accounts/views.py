from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        messages.success(request, 'Welcome to StockSense!')
        return redirect('home')
    return render(request, 'auth.html', {'form': form, 'title': 'Register'})
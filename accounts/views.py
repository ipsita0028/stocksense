from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.groups.add(Group.objects.get(name='Staff'))
        login(request, user)
    return render(request, 'auth.html', {'form': form, 'title': 'Register'})
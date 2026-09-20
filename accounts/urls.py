from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        authentication_form=LoginForm, template_name='auth.html',
        extra_context={'title': 'Login'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
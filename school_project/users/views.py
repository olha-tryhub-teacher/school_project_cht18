from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'login:login.html'

class UserCreationView(CreateView):
    template_name = 'login/register.html'
    form_class = UserCreationForm




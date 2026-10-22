from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'login:login.html'

class UserCreationView(CreateView):
    template_name = 'login/register.html'
    form_class = UserCreationForm

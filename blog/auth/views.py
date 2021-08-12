from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class loginView(auth_views.LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    pass
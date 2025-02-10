from django.contrib import admin
from .models import *
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import CustomLoginForm

class CustomAdminLoginView(auth_views.LoginView):
    template_name = 'admin/login.html' 
    authentication_form = CustomLoginForm

admin.site.login = CustomAdminLoginView.as_view()


admin.site.register(Video_type)
admin.site.register(Video)
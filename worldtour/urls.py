"""
URL configuration for worldtour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from asiantoursagency import views as asian_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Tours app URLs - includes all auth-related URLs
    path('', include('asiantoursagency.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/register/', asian_views.register_view, name='register'),
]

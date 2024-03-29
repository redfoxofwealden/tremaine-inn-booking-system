"""
URL configuration for tremaineinn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from customeraccount import views as customer_views
from . import views as main_views

urlpatterns = [
    path('', main_views.home_views, name='home'),
    path('register/', customer_views.register, name='register'),
    path('sign-in/', customer_views.sign_in, name='sign-in'),
    path('admin/', admin.site.urls),
]

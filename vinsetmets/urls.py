"""vinsetmets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'cuisines/', include('cuisines.urls', namespace='cuisines'), name='cuisines'),
    path(r'products/', include('products.urls', namespace='products'), name='products'),
    path(r'wines/', include('wines.urls', namespace='wines'), name='wines')
]

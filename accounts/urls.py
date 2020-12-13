from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("main", views.main, name='main'),
    path("shop", views.shop, name='shop'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path("single", views.single, name='single'),
    path("o404", views.o404, name='o404'),
    path("", views.index, name='index'),
    ]

from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('accueil/', views.accueil),
    path('articles/', views.accueil),
    path('contact/', views.contact),
]

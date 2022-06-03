
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name="home"),
    path('articles/', views.articles, name="article"),
    path('contact/', views.contact, name="contact"),
    path('utilisateurs/', include('utilisateurs.urls')),
]

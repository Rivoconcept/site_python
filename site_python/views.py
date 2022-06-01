from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
     return HttpResponse('Bonjour tout le monde')

def acceuil(request):
    return render(request, "accueil.html")

def articles(request):
    return render(request, "articles.html")

def contact(request):
    return render(request, "contact.html")
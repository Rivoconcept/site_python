from django.http import HttpResponse
from django.shortcuts import render

def accueil(request):
    return render(request, "accueil.html")

def articles(request):
    return render(request, "articles.html")

def contact(request):
    return render(request, "contact.html")
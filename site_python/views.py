
from django.shortcuts import render
from .db_art import arts

    
def accueil(request):
    return render(request, "accueil.html")

def articles(request):
    return render(request, "articles.html", context = {'arts':arts})

def contact(request):
    return render(request, "contact.html")
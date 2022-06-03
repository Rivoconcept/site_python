
from django.shortcuts import render
from .db_arts import arts


def articles(request):
    return render(request, 'articles/liste.html', context = {'arts':arts})


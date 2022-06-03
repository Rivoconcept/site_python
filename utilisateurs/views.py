from django.shortcuts import render
from django.http import HttpResponse


def utilisateurs(request):
    return render(request, 'utilisateurs.html')
    # return HttpResponse("user")
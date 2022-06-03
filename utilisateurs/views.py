from django.shortcuts import render



def utilisateurs(request):
    return render(request, 'utilisateurs/liste.html')
   
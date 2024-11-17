from django.shortcuts import render

def index(request):
    nom = ""
    dec = ""
    return render(request, "blog/index.html",{"nom": nom, "dec": dec})
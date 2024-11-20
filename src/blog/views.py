from django.shortcuts import render
from .models import *

def index(request):
    creations = Creation.objects.all()
    return render(request, "blog/index.html",{"creations": creations})
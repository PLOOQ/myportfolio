
from django.views import View
from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, "fields/index.html")

def webdev(request):
    return render(request, "fields/webdev.html")

def GameDev(request):
    return render(request, "fields/gamedev.html")

def Cybersecurity(request):
    return render(request, "fields/cybersecurity.html")

def ArtificialIntelligence(request):
    return render(request, "fields/artificialintelligence.html")

def ContactInfo(request):
    return render(request, "fields/contactinfo.html")

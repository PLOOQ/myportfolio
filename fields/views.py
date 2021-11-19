
from django.views import View
from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, "fields/Index.html")

def WebDev(request):
    return render(request, "fields/WebDev.html")

def GameDev(request):
    return render(request, "fields/GameDev.html")

def Cybersecurity(request):
    return render(request, "fields/Cybersecurity.html")

def ArtificialIntelligence(request):
    return render(request, "fields/ArtificialIntelligence.html")

def ContactInfo(request):
    return render(request, "fields/ContactInfo.html")

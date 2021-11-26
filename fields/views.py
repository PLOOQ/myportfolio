
from django.views import View
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "fields/index.html")

def web_dev(request):
    return render(request, "fields/web-dev.html")

def game_dev(request):
    return render(request, "fields/game-dev.html")

def cyber_security(request):
    return render(request, "fields/cyber-security.html")

def artificial_intelligence(request):
    return render(request, "fields/artificial-intelligence.html")

def contact_info(request):
    return render(request, "fields/contact-info.html")

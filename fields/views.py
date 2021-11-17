
from django.views import View
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "fields/index.html")
    
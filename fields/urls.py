from django.urls import path

from .views import WebDev, GameDev, Cybersecurity,ArtificialIntelligence,ContactInfo, Index

urlpatterns = [
    path('',Index, name="index"),
    path('webdev',WebDev, name="webdev"),
    path('gamedev',GameDev, name="gamedev"),
    path('cybersecurity',Cybersecurity, name="cybersecurity"),
    path('artificialintelligence',ArtificialIntelligence, name="artificialintelligence"),
    path('contactinfo',ContactInfo, name="contactinfo"),
    
]

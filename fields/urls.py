from django.urls import path

from .views import WebDev, GameDev, Cybersecurity,ArtificialIntelligence,ContactInfo, Index

urlpatterns = [
    path('',Index, name="Index"),
    path('WebDev',WebDev, name="WebDev"),
    path('GameDev',GameDev, name="GameDev"),
    path('Cybersecurity',Cybersecurity, name="Cybersecurity"),
    path('ArtificialIntelligence',ArtificialIntelligence, name="ArtificialIntelligence"),
    path('ContactInfo',ContactInfo, name="ContactInfo"),
    
]

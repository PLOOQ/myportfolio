from django.urls import path
from .views import Webdev, GameDev, Cybersecurity,ArtificialIntelligence,ContactInfo, Index

urlpatterns = [
    path('index',Index, name="index"),
    path('webdev',Webdev, name="webdev"),
    path('gamedev',GameDev, name="gamedev"),
    path('cybersecurity',Cybersecurity, name="cybersecurity"),
    path('artificialintelligence',ArtificialIntelligence, name="artificialintelligence"),
    path('contactinfo',ContactInfo, name="contactinfo"),
    
]

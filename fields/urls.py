from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name="index"),
    path('webdev',views.webdev, name="web-dev"),
    path('gamedev',views.gamedev, name="game-dev"),
    path('cybersecurity',views.cybersecurity, name="cyber-security"),
    path('artificialintelligence',views.artificialintelligence, name="artificial-intelligence"),
    path('contactinfo',views.contactInfo, name="contact-info"),
    
]

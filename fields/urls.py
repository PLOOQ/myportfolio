from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name="index"),
    path('webdev',views.web_dev, name="web-dev"),
    path('gamedev',views.game_dev, name="game-dev"),
    path('cybersecurity',views.cyber_security, name="cyber-security"),
    path('artificialintelligence',views.artificial_intelligence, name="artificial-intelligence"),
    path('contactinfo',views.contact_info, name="contact-info"),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('devweb',views.dev_web, name="dev-web"),
    path('gamedev',views.game_dev, name="game-dev"),
    path('cybersecurity',views.cyber_security, name="cyber-security"),
    path('artificialintelligence',views.artificial_intelligence, name="artificial-intelligence"),
    path('contactinfo',views.contact_info, name="contact-info"),
    
]

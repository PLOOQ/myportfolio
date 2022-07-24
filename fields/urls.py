from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('softdev',views.soft_dev, name="software-development"),
    path('cybersecurity',views.cyber_security, name="cyber-security"),
    path('artificialintelligence',views.artificial_intelligence, name="artificial-intelligence"),
    path('contactinfo',views.contact_info, name="contact-info"),
    
]

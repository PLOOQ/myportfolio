from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('softeng',views.soft_eng, name="software-engineering"),
    path('cybersecurity',views.cyber_security, name="cyber-security"),
    path('artificialintelligence',views.artificial_intelligence, name="artificial-intelligence"),
    path('contactinfo',views.contact_info, name="contact-info"),
    
]

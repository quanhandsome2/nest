from django.urls import path
from . import views


app_name= "store"

urlpatterns = [
    path('', views.index, name="index"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
]

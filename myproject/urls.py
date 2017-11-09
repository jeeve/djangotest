from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^accueil$', views.home),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home import views

urlpatterns = [
    path('', views.home, name='home'),
]

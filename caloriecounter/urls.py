from django.contrib import admin
from django.urls import path

from caloriecounter import views

urlpatterns = [
    path('', views.home, name='home'),
]

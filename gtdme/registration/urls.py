from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('registration/', views.registration),
    path('authorization/', views.authorization)
]

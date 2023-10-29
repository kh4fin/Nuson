from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistik/', views.statistik, name='statistik'),
]


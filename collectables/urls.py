from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bugs),
    path('fish/', views.fish),
    path('sea_creatures/', views.sea_creatures),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('desktops/', views.browse_desktops, name="browse_desktops"),
    path('laptops/', views.browse_laptops, name="browse_laptops")
]

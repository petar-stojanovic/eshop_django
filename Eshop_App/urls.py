from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('desktops/', views.browse_desktops, name="browse_desktops"),
    path('desktop/<int:id>', views.customize_desktop, name="customize_desktop"),
    path('laptops/', views.browse_laptops, name="browse_laptops"),
    path('laptop/<int:id>', views.customize_laptop, name="customize_laptop"),
    path('checkout/<str:platform>/<int:id>?<int:order_id>', views.checkout_page, name="checkout"),
    path('received/<str:platform>/<int:id>', views.receive_order, name="receive_order"),
]

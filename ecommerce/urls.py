from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Site-Home'),
    path('about/', views.about, name='Site-About'),
    path('cart/', views.cart, name='Site-Cart'),
    path('myorders/', views.myorders, name='Site-Orders'),
    path('mobile_cov/', views.mobile_cover, name='site-mobilecover'),
    path('ordered/', views.ordered, name='ordered'),
    path('laptop_cov/', views.laptop_cover, name='site-laptopcover'),
    path('paintings/', views.art, name='site-art'),
    path('clothing/', views.clothing, name='site-clothing'),

    
]

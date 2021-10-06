
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from store.views import *
urlpatterns = [
    path('', home, name="home"),
    path('cart/', cart, name="cart"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('orders/', orders, name="orders"),
    path('logout/',logout,name='logout'),
    path('checkout/',checkout,name='checkout'),
    path('validate_payment/',validatePayment,name='validatePayment'),

 
    path('product/<str:slug>/',show_product,name='show_product'),
    path('addtocart/<str:slug>/<str:size>',add_to_cart,name='add_to_cart'),


    
]

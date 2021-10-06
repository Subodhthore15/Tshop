from store.forms.checkout_form import CheckForm
from django.contrib.auth import authenticate, login as LoginUser, logout as logout_USER
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from store.models import Brand, Color, IdealFor, NeckType, Occasion, Order, OrderItem, Payment, Sleeve,Tshirt, SizeVarient, Cart
import math as m
from django.contrib.auth.decorators import login_required
from ECommerceShop.settings import API_KEY,AUTH_TOKEN
from instamojo_wrapper import Instamojo



@login_required(login_url='login')
def orders(request):
    user= request.user
    orders=Order.objects.filter(user = user).order_by('-date').exclude(order_status="PENDING")
    # orders=OrderItem.objects.filter(order = order)
    # print(orders)
    return render(request, 'store/orders.html',{'orders':orders})

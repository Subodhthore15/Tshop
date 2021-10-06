from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from store.models import Brand, Color, IdealFor, NeckType, Occasion, Order, OrderItem, Payment, Sleeve,Tshirt, SizeVarient, Cart
import math as m
from django.contrib.auth.decorators import login_required
from ECommerceShop.settings import API_KEY,AUTH_TOKEN
from instamojo_wrapper import Instamojo



API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')




def show_product(request, slug):
    tshirt_de = Tshirt.objects.get(slug=slug)

    actual_size = request.GET.get('size')  # it gives size string

    if actual_size is None:  # by default minimum price show
        size = tshirt_de.sizevarient_set.all().order_by('price').first()

    else:
        size = tshirt_de.sizevarient_set.get(size=actual_size)

    actual_price = size.price

    active_size = size

    selling_price = actual_price-(actual_price * (tshirt_de.discount/100))

    return render(request, 'store/product_details.html', context={'tshirt': tshirt_de, 'price': actual_price, 'sell_price': selling_price, 'active_size': active_size})




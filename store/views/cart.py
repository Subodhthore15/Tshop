
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


def cart(request):
    # IF user is not logged in we store the action in session.
    cart = request.session.get('cart')  # it return list of objects

    if cart is None:
        cart = []

    for c in cart:  # c is object
        tshirt_id = c.get('tshirt')

        # it gives that tshirt from database
        tshirt = Tshirt.objects.get(id=tshirt_id)

        # fetch size object bcz it contain price.
        c['size'] = SizeVarient.objects.get(tshirt=tshirt, size=c['size'])

        c['tshirt'] = tshirt  # id is replace with tshirt

    print(cart)

    return render(request, 'store/cart.html', context={'cart': cart})


def add_to_cart(request, slug, size):
    user = None
    if request.user.is_authenticated:
        user = request.user
    # print(slug," ",size)
    cart = request.session.get('cart')  # initiallly None

    if cart is None:
        cart = []  # it will be contain list of objects

    tshirt = Tshirt.objects.get(slug=slug)

    add_to_cart_for_anonom_user(cart, size, tshirt)

    if user is not None:
        add_cart_to_database(user, size, tshirt)

    # make cart key and assign cart list of objects to it
    request.session['cart'] = cart

    # process return_url
    # return on that url on which you click
    return_url = request.GET.get('return_url')

    return redirect(return_url)


# When User is logged in then store into the database
def add_cart_to_database(user, size, tshirt):
    size_temp = SizeVarient.objects.get(size=size, tshirt=tshirt)

    # Existin cart
    # Return list of value if contain
    existing = Cart.objects.filter(user=user, sizeVarient=size_temp)
    if len(existing) > 0:
        obj = existing[0]
        obj.quantity += 1
        obj.save()
    else:
        c = Cart()
        c.user = user
        c.sizeVarient = size_temp
        c.quantity = 1
        c.save()


# When user is not  logged in save it in session variable
def add_to_cart_for_anonom_user(cart, size, tshirt):

    flag = True
    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        size_short = cart_obj.get('size')
        if t_id == tshirt.id and size_short == size:
            flag = False
            cart_obj['quantity'] += 1

    if flag:
        cart_obj = {
            'tshirt': tshirt.id,
            'size': size,
            'quantity': 1  # when you click on buttton quantity becomes 1.

        }
        cart.append(cart_obj)

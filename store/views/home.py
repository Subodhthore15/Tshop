
from django.db.models.query_utils import Q
from store.forms.checkout_form import CheckForm
from django.contrib.auth import authenticate, login as LoginUser, logout as logout_USER
from store.forms.authforms import CustomerCreationForm, CustomerAuthForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from store.models import Brand, Color, IdealFor, NeckType, Occasion, Order, OrderItem, Payment, Sleeve,Tshirt, SizeVarient, Cart, tshirt
import math as m
from django.contrib.auth.decorators import login_required
from ECommerceShop.settings import API_KEY,AUTH_TOKEN
# from instamojo_wrapper import Instamojo

# Pagination
from django.core.paginator import Paginator
from urllib.parse  import urlencode


def home(request):

    query=request.GET

    tshirts=[] 

    tshirts = Tshirt.objects.all()
    brand = query.get('brand')
    neckType = query.get('necktype')
    color = query.get('color')
    idealFor = query.get('idealfor')
    sleeve = query.get('sleeve')

    page= query.get('page')
    if(page is None or page==''):
        page=1

    

    

    

    if brand != '' and brand is not None:
        tshirts = tshirts.filter(brand__slug=brand)
    if neckType != '' and neckType is not None:
        tshirts = tshirts.filter(neck_type__slug=neckType)
    if color != '' and color is not None:
        tshirts = tshirts.filter(color__slug=color)
    if sleeve != '' and sleeve is not None:
        tshirts = tshirts.filter(sleeve__slug=sleeve)
    if idealFor != '' and idealFor is not None:
        tshirts = tshirts.filter(ideal_for__slug=idealFor)
    

    occasions= Occasion.objects.all()
    brands = Brand.objects.all()
    sleeves= Sleeve.objects.all()
    idealfor=IdealFor.objects.all()
    necktypes= NeckType.objects.all()
    colors = Color.objects.all()


    
    paginator = Paginator(tshirts,4) # On one page 4 object(tshirts) you want to show

    page_object=paginator.get_page(page)  # get first page that contain 4 objects

    query = request.GET.copy()
    query['page'] = ""
    # Dictinary is converted into query string.
    pageurl=urlencode(query)
    print(query)
    context = {
    'page_obj': page_object, # pass page object here
    'occasions':occasions,
    'brands':brands,
    'sleeves':sleeves,
    'idealfor':idealfor,
    'necktypes':necktypes,
    'colors':colors,
    'pageurl':pageurl
    }
    cart = request.session.get('cart')
    # print(cart)

    

    return render(request, 'store/home.html', context=context)

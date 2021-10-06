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



API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')



def total_payable_amount(cart):
    total = 0
    for c in cart:
        discount = c.get('tshirt').discount
        price = c.get('size').price
        sale_price = m.floor(price - (price * (discount / 100)))
        total_of_single_product = sale_price * c.get('quantity')
        total = total + total_of_single_product

    return total




@login_required(login_url='login')
def checkout(request):
    # Handle get Request first
    if request.method == "GET":
        obj = CheckForm()
        cart = request.session.get('cart')
        if cart is None:
            cart = []

        for c in cart:
            size_str = c.get('size')
            tshirt_id = c.get('tshirt')
            # Now Size key contain Sizevarient object that contain
            # both tshirt and price
            size_obj = SizeVarient.objects.get(size=size_str, tshirt=tshirt_id)
            c['size'] = size_obj
            c['tshirt'] = size_obj.tshirt

        return render(request, 'store/checkout.html', {'checkform': obj, 'cart': cart})


    elif request.method=="POST": # when form is submitted
        form = CheckForm(request.POST)


        # Getting Logged in user
        user= None
        if request.user.is_authenticated:
            user = request.user
        if form.is_valid():
            # payment
            cart = request.session.get('cart')
            if cart is None:
                cart=[]
            for c in cart:
                size_str = c.get('size')
                tshirt_id = c.get('tshirt')
                # Now Size key contain Sizevarient object that contain
                # both tshirt and price
                size_obj = SizeVarient.objects.get(size=size_str, tshirt=tshirt_id)
                c['size'] = size_obj
                c['tshirt'] = size_obj.tshirt



            shipping_address=form.cleaned_data.get('shipping_addresss')
            phone=form.cleaned_data.get('phone')
            payment_method=form.cleaned_data.get('payment_method')

            total=total_payable_amount(cart)

            order=Order()
            order.shipping_addresss= shipping_address
            order.total = total
            order.payment_method = payment_method
            order.phone = phone
            order.order_status = "PENDING"
            order.user = user
            order.save()

            # print(shipping_address," ",phone," ",payment_method," ", total)

            # Store all the item of the user in OrderItem table
            
            for c in cart:
                order_item= OrderItem()
                order_item.order = order
                size=c.get('size')
                tshirt=c.get('tshirt')


                

                order_item.price = m.floor(size.price -
                                         (size.price *
                                          (tshirt.discount / 100)))
                order_item.quantity = c.get('quantity')
                order_item.size = size
                order_item.tshirt = tshirt
                order_item.save()

            
            # Making payment

            response = API.payment_request_create(
                     amount=order.total,
                     purpose='Payment for Tshirts',
                     send_email=True,
                     email=user.email,
                    
                    # send_sms = True, it gives error
                    
                     buyer_name = f"{user.first_name} {user.last_name }",
                 redirect_url="http://localhost:8000/validate_payment"
            )

            payment_request_id= response['payment_request']['id']

            # By this url link client make payment . After checkout we navigateb here
            url = response['payment_request']['longurl']

            payment= Payment()
            payment.order = order
            payment.payment_request_id =  payment_request_id
            payment.save()

            return redirect(url)

        else:
            return redirect('checkout')

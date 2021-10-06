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


def validatePayment(request):
    user=None
    # Gettting logged in user
    if request.user.is_authenticated:
        user= request.user
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    print(payment_request_id," ",payment_id )
    response = API.payment_request_payment_status(payment_request_id, payment_id)
    status = response.get('payment_request').get('payment').get('status')

    # print(status)  
    if status != "Failed":
        print("Payment success")
        try:

            payment= Payment.objects.get(payment_request_id =payment_request_id )
        
            payment.payment_id =payment_id
            payment.payment_status = status
            payment.save()

            # order status update
            order=payment.order
            order.order_status= "PLACED"
            order.save()


            # Clearing cart empty bcz it's payment has been done
            # 1] Deleting from session
            cart=[]
            request.session['cart']=cart 

            # 2] deleting from database table cart
            Cart.objects.filter(user= user).delete()

            return redirect('orders')
        except:
            return render(request,'store/payment_failed.html')
    else:
        return render(request,'store/payment_failed.html')
        # Erroe message

    # return HttpResponse(status)


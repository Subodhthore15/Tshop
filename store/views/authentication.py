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


def login(request):
    if(request.method == "GET"):
        form = CustomerAuthForm()

        # Login kelayver checkout page kadhnayasthi
        next_page = request.GET.get('next')
        if next_page is not None:

            request.session['next_page'] = next_page

        return render(request, 'store/login.html', {'form': form})

    else:
        form = CustomerAuthForm(data=request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                LoginUser(request, user)

                # When user logged in at that time session data also need to add in database - cart
                session_cart = request.session.get('cart')

                if session_cart is None:
                    session_cart = []
                else:
                    for c in session_cart:
                        size = c.get('size')
                        tshirt_id = c.get('tshirt')

                        quantity = c.get('quantity')
                        cart_obj = Cart()
                        cart_obj.sizeVarient = SizeVarient.objects.get(
                            size=size, tshirt=tshirt_id)
                        cart_obj.quantity = quantity
                        cart_obj.user = user
                        cart_obj.save()

                # We need to add this to sessions
                # {size,thirt,quantity}
                cart = Cart.objects.filter(user=user)
                session_cart = []
                for c in cart:
                    obj = {
                        "size": c.sizeVarient.size,
                        "tshirt": c.sizeVarient.tshirt.id,
                        "quantity": c.quantity
                    }
                    session_cart.append(obj)

                request.session['cart'] = session_cart

                next_page = request.session.get('next_page')
                if next_page is None:
                    next_page = "home"

                return redirect(next_page)
            else:
                return render(request, 'store/login.html', {'form': form})

        else:
            return render(request, 'store/login.html', {'form': form})


def signup(request):

    if(request.method == "GET"):
        form = CustomerCreationForm()
        context = {
            'form': form
        }
        return render(request, 'store/signup.html', context=context)

    else:  # Post - > Store Data in the database/Register user.
        form = CustomerCreationForm(request.POST)

        if(form.is_valid()):  # Store to the database
            user = form.save()
            user.email = user.username
            user.save()

            return redirect('login')

        else:  # Show user what's wrong.
            context = {
                'form': form
            }
        return render(request, 'store/signup.html', context=context)



def logout(request):
    logout_USER(request)
    return redirect('home')

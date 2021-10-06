import django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms
from django.forms import fields, models # use of form api
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from store.models import Order



class CheckForm(forms.ModelForm): # Make form according to model(table)
    class Meta:
        model = Order # use  Order model 

        # Which field you  want to show user from that form model
        fields=['shipping_addresss','phone','payment_method']

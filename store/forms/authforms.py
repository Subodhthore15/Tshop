import django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms
from django.forms import fields, models # use of form api
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


#Inheritacne of UserCreationForm->Signup form
class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True,label="Email")
    first_name = forms.CharField(required=True,label="First name")
    last_name = forms.CharField(required=True,label="Last name")


    def clean_first_name(self):
        value=self.cleaned_data.get('first_name')
        if(len(value)<4):
            raise ValidationError("Enter named must be greater than 4 character!")
        
        return value

        
    class Meta:
        # where to store form data, mention in the model=User
        model  = User

        fields = ['username','first_name','last_name']
        # Firstname,lastname already present in the User



# Inheritace for login form 

class CustomerAuthForm(AuthenticationForm):
    username = forms.EmailField(required=True,label="Email")
    
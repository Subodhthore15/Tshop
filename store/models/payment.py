
from enum import Flag
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.
from store.models import *

class Payment(models.Model):
    order = models.ForeignKey(Order , on_delete = models.CASCADE)
    date = models.DateTimeField(null= False , auto_now_add=True)
    payment_status = models.CharField(max_length=15 , default='FAILED')
    payment_id = models.CharField(max_length=60) #Gets after payment has succesfully done
    payment_request_id = models.CharField(max_length=60 , unique=True , null=False) # Gets initially

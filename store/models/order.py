from enum import Flag
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.
from store.models import *



class Order(models.Model):
    orderChoices=[
        # (" we use this for operation","user/admin sees it")
        ("PENDING", "pending"),
        ("PLACED", "placed"),
        

        ("CANCELED", "canceled"),
        ("COMPLETED", "completed"),
        
    ]
    method=[
        # (" we use this for operation","user/admin sees it")
        ("COD", "cod"),
        ("ONLINE", "online"),
      
        
    ]

    order_status = models.CharField(max_length=15, choices=orderChoices)
    payment_method = models.CharField(max_length=15, choices=method)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(null=False)
    date = models.DateTimeField(null=False,auto_now_add=True)
    shipping_addresss = models.CharField(max_length=15, null=False)
    phone = models.CharField(max_length=10, null=False)
    


class OrderItem(models.Model):

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt,on_delete=models.CASCADE)

    size =  models.ForeignKey(SizeVarient,on_delete=models.CASCADE)

    quantity = models.IntegerField(null=False)

    price = models.IntegerField(null=False)

    date = models.DateTimeField(null=False,auto_now_add=True)

    def __str__(self):
        return self.tshirt.name
        
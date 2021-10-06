from enum import Flag
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.
from store.models import *

class Cart(models.Model):
    
    sizeVarient = models.ForeignKey(SizeVarient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
   
    # def __str__(self):
    #     return self.sizeVarient.tshirt.name

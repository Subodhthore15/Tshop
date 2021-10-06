from enum import Flag
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.
from store.models import *

class SizeVarient(models.Model):
    price = models.IntegerField(null=False)  # not null

    # after SizeVarient record is  deleted  tshirt also need to be deleted
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)

    # we want to give choices to user/admin to select size
    SIZES = [
        # (" we use this for operation","user/admin sees it")
        # ("database Store","user ko dikhana")
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra large"),
        ("XXL", "Extra Extra large"),
    ]

    size = models.CharField(choices=SIZES, max_length=5)
    def __str__(self):
        return f'{self.size}'

from enum import Flag
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.

# using inheritance here


from store.models import *

class Tshirt(models.Model):
    name = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=200,unique=True,default="")

    # if we don't fill desciption, it doesn't matter for this now.
    description = models.CharField(max_length=30, null=True)
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to="upload/images", null=False)

    # on_delete -> when occasion is deleted releated record is deleted in tshirt.
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    neck_type = models.ForeignKey(NeckType, on_delete=models.CASCADE)
    ideal_for = models.ForeignKey(IdealFor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


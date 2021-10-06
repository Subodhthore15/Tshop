from enum import Flag
from django.db import models

from django.contrib.auth.models import User
from django.db.models.enums import Choices

class TshirtProperty(models.Model):
    title = models.CharField(max_length=30, null=False)
    slug = models.CharField(max_length=30, null=False, unique=True)

    # Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields/class

    # we don't want to create table for this class
    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Occasion(TshirtProperty):
    pass


class IdealFor(TshirtProperty):
    pass


class NeckType(TshirtProperty):
    pass


class Sleeve(TshirtProperty):
    pass


class Brand(TshirtProperty):
    pass


class Color(TshirtProperty):
    pass

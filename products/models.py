from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True)
    cost = models.IntegerField(default=0)
    ordered = models.IntegerField(default=0)

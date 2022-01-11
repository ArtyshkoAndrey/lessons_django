from django.db import models

from brands.models import Brand
from categories.models import Category


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True)
    cost = models.IntegerField(default=0)
    ordered = models.IntegerField(default=0)
    brand = models.ForeignKey(
        Brand,
        null=True,
        on_delete=models.SET_NULL,
        primary_key=False,
        related_name='products'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        primary_key=False,
        related_name = 'products'
    )

    def __str__(self):
        return str(self.id) + " - " + self.name

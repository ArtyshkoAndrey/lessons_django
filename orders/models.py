from django.db import models

from customers.models import Customer
from products.models import Product


# Create your models here.
class Order(models.Model):
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return "Заказ №" + str(self.id) + " от " + self.user.name
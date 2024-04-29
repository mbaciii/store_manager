from django.db import models

# Create your models here.
from django.db import models
import datetime


class Product(models.Model):
    name = models.CharField(max_length=100)
    # Add any other necessary fields for the product



class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_code = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=datetime.datetime.now)


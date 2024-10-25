# models.py
from django.db import models

class Product(models.Model):
    product_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    compliance = models.BooleanField()  # Assuming compliance is a boolean
    past_performance = models.FloatField()  # Historical performance score

    def __str__(self):
        return self.product_name

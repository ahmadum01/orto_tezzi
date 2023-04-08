from django.db import models

from .product_type import ProductType


class Product(models.Model):
    GENDER_CHOICES = (
        ("M", "Man"),
        ("W", "Women"),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products", blank=True, null=True)
    price = models.IntegerField()
    size = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

from django.db import models

from .product_type import ProductType

from django.utils.html import mark_safe

class Product(models.Model):
    GENDER_CHOICES = (
        ("M", "Man"),
        ("W", "Women"),
        ("C", "Common"),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products", blank=True, null=True)
    price = models.IntegerField()
    sizes = models.ManyToManyField("products.ProductSize", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.image)

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

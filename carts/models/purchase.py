from django.db import models

from products.models import Product


class Purchase(models.Model):
    GENDER_CHOICES = (
        ("M", "Man"),
        ("W", "Women"),
        ("C", "Common"),
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    size = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)
    gender = models.CharField(
        choices=Product.GENDER_CHOICES, max_length=10, default="C"
    )

    def __str__(self):
        return self.product.name

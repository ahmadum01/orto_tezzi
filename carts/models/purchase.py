from django.db import models


class Purchase(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    size = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

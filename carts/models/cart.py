from django.db import models


class Cart(models.Model):
    purchases = models.ManyToManyField("carts.Purchase", null=True, blank=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

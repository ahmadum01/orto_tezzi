from dataclasses import dataclass

from .. import models


@dataclass
class PurchaseToCartAdder:
    purchase_id: int
    user: any

    def execute(self):
        purchase = models.Purchase.objects.get(pk=self.purchase_id)
        cart = models.Cart.objects.get(user=self.user)
        cart.purchases.add(purchase)

import factory
from factory.django import DjangoModelFactory

from products.tests.factories import ProductFactory

from .. import models


class CartFactory(DjangoModelFactory):
    class Meta:
        model = models.Cart


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = models.Purchase

    product = factory.SubFactory(ProductFactory)
    cart = factory.SubFactory(CartFactory)

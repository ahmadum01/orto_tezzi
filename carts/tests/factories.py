from factory.django import DjangoModelFactory
import factory
from .. import models
from products.tests.factories import ProductFactory


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = models.Purchase
    product = factory.SubFactory(ProductFactory)


class CartFactory(DjangoModelFactory):
    class Meta:
        model = models.Cart

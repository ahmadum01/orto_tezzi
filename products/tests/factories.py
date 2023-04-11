import factory.fuzzy
from factory.django import DjangoModelFactory

from .. import models


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = models.Product
    price = factory.fuzzy.FuzzyInteger(1, 10)

class ProductTypeFactory(DjangoModelFactory):
    class Meta:
        model = models.ProductType


class ProductSizeFactory(DjangoModelFactory):
    class Meta:
        model = models.ProductSize
    size = 15

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .. import models
from . import serializers


class ProductViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

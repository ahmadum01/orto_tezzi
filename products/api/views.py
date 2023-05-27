from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .. import models
from . import filters, serializers


class ProductViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductsFilter

    # @action(
    #     methods=('GET',),
    #     detail=False,
    # )
    # def product_type(self):
    #     return Response(data={"tags": })


class ProductTypeViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer

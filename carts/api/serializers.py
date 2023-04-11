from rest_framework import serializers

from products.api.serializers import ProductSerializer

from .. import models


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        read_only_fields = ("id",)
        fields = (
            *read_only_fields,
            "product",
            "size",
            "quantity",
        )
        product = ProductSerializer()

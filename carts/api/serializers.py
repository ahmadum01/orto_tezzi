from rest_framework import serializers
from .. import models
from products.api.serializers import ProductSerializer


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        read_only_fields = ('id',)
        fields = (
            *read_only_fields,
            'product',
            'size',
            'quantity',
        )
        product = ProductSerializer()
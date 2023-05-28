from rest_framework import serializers

from products.api.serializers import ProductSerializer
from products.models import Product

from .. import models


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        read_only_fields = ("id", "product")
        fields = (
            *read_only_fields,
            "product_id",
            "size",
            "quantity",
            "gender",
        )

    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    def validate_size(self, size):
        try:
            purchase_pk = int(self.context["request"].parser_context["kwargs"]["pk"])
            product = models.Purchase.objects.get(pk=purchase_pk).product
        except KeyError:
            product_pk = self.context["request"].data["product_id"]
            product = Product.objects.get(pk=product_pk)
        sizes = product.sizes.all()
        if size not in [product_size.size for product_size in sizes]:
            raise serializers.ValidationError("This size doesn't exist!")
        return size

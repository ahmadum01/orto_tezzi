from rest_framework import serializers

from .. import models


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductType
        fields = ("name",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        read_only_fields = ('id',)
        fields = (
            *read_only_fields,
            'name',
            'description',
            'image',
            'price',
            'sizes',
            'gender',
            'product_type',
        )

    sizes = serializers.SerializerMethodField()

    def get_sizes(self, product: models.Product) -> list[int]:
        return [size.size for size in product.sizes.all()]

    product_type = serializers.CharField(source="product_type.name", required=False)

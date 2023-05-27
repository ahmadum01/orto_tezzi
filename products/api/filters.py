import django_filters.rest_framework as filtersets


class ProductsFilter(filtersets.FilterSet):
    product_type = filtersets.CharFilter(
        field_name="product_type__name",
    )
    ordering = filtersets.OrderingFilter(
        # tuple-mapping retains order
        fields=(("price", "price"), ("name", "name"), ("created_at", "created_at")),
    )

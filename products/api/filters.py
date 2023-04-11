import django_filters.rest_framework as filtersets
from django.utils.translation import gettext_lazy as _


class ProductsFilter(filtersets.FilterSet):
    product_type = filtersets.CharFilter(
        field_name='product_type__name',
    )
    ordering = filtersets.OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('price', 'price'),
            ('name', 'name'),
        ),
    )
    #
    # def filter_queryset(self, queryset):
    #     breakpoint()


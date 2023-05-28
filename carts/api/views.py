import rest_framework.serializers as drf_serializers
from django.db.models import Sum
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from drf_spectacular.utils import extend_schema, inline_serializer

from .. import models
from . import serializers


class PurchaseViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # add purchase to card
        user = request.user
        serializer.validated_data["cart"] = models.Cart.objects.get(user=user)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @extend_schema(
        responses=inline_serializer(
            name="BrandMediaFilterSerializer",
            fields={
                "review": drf_serializers.IntegerField(),
                "accepted": drf_serializers.IntegerField(),
                "favorites": drf_serializers.IntegerField(),
                "rejected": drf_serializers.IntegerField(),
            },
        ),
    )
    @action(
        methods=("GET",),
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def cart_statistic(self, request):
        queryset = self.get_queryset()
        quantity = queryset.count()
        price_sum = queryset.aggregate(Sum("product__price"))["product__price__sum"]
        response = {
            "quantity": quantity,
            "price_sum": price_sum,
        }
        return Response(response, status=200)

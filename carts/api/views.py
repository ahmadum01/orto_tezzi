import rest_framework.serializers as drf_serializers
from django.db.models import F, Sum
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
        return self.queryset.filter(cart__user=self.request.user, quantity__gt=0)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        purchases = self.queryset.filter(
            cart__user=user,
            gender=serializer.validated_data["gender"],
            size=serializer.validated_data["size"],
        )
        if purchases.exists():
            purchase = purchases.first()
            purchase.quantity = F("quantity") + serializer.validated_data["quantity"]
            purchase.save(update_fields=["quantity"])
        else:
            # add purchase to card
            serializer.validated_data["cart"] = models.Cart.objects.get(user=user)
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @extend_schema(
        responses=inline_serializer(
            name="CartStatisticSerializer",
            fields={
                "quantity": drf_serializers.IntegerField(),
                "price_sum": drf_serializers.IntegerField(),
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
        quantity = queryset.aggregate(common_quantity=Sum("quantity"))[
            "common_quantity"
        ]
        price_sum = queryset.aggregate(
            price_sum=Sum(F("product__price") * F("quantity"))
        )["price_sum"]
        response = {
            "quantity": quantity,
            "price_sum": price_sum,
        }

        return Response(response, status=200)

    @action(
        methods=("DELETE",),
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def clear(self, request):
        self.get_queryset().delete()
        return Response({"Success": True}, status=204)

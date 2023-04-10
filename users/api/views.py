from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from .. import models
from . import serializers


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    @action(
        methods=["get"],
        detail=False,
        serializer_class=serializers.UserSerializer,
        permission_classes=[IsAuthenticated],
    )
    def self(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(data=serializer.data, status=200)

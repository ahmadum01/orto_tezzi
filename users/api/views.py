from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

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

    @extend_schema(responses={200: AuthTokenSerializer})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = models.User.objects.create_user(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key}, status=201)

from rest_framework import serializers

from .. import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "username",
            "password",
            "full_name",
            "phone_number",
        )

    password = serializers.CharField(max_length=255, write_only=True)

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return models.User.objects.create_user(**validated_data)

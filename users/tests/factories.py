from factory.django import DjangoModelFactory

from users import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

from rest_framework.test import APIClient
import pytest
from users.tests import factories


@pytest.fixture()
def user():
    return factories.UserFactory()


@pytest.fixture
def logged_client(user):
    client = APIClient()
    client.force_authenticate(user)
    return client

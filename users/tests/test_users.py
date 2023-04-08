import pytest
from . import factories
from ..models import User


@pytest.mark.django_db
def test_user_create():
    factories.UserFactory()
    assert User.objects.count() == 1


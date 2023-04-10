import pytest

from ..models import User
from . import factories


@pytest.mark.django_db
def test_user_create():
    """test"""
    factories.UserFactory()
    assert User.objects.count() == 1

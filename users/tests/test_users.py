import pytest
from rest_framework.authtoken.models import Token

from carts.models import Cart


@pytest.mark.django_db
def test_user_create(client):
    payload = {
        'username': 'John_Doe',
        'password': '1' * 10
    }
    response = client.post('/user/', data=payload)
    assert response.status_code == 201
    data = response.json()
    token = Token.objects.get().key
    assert data['token'] == token
    assert Cart.objects.filter(user__username=payload['username']).count() == 1


@pytest.mark.django_db
def test_user_get_self(user, logged_client):
    user.username = "John Doe"
    user.save()
    response = logged_client.get('/user/self/')
    assert response.status_code == 200
    data = response.json()
    assert data['username'] == user.username


@pytest.mark.django_db
def test_user_unauthorized_get_self(client):
    response = client.get('/user/self/')
    assert response.status_code == 401





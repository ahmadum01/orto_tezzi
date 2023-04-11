import pytest
from . import factories
from products.tests.factories import ProductFactory
from ..models import Purchase


@pytest.mark.django_db
def test_purchase_list(user, logged_client):
    cart = factories.CartFactory(user=user)
    for _ in range(10):
        cart.purchases.add(factories.PurchaseFactory())

    response = logged_client.get('/cart/')
    assert response.status_code == 200

    data = response.json()
    assert data['count'] == 10


@pytest.mark.django_db
def test_purchase_destroy(user, logged_client):
    cart = factories.CartFactory(user=user)
    purchase = factories.PurchaseFactory()
    cart.purchases.add(purchase)

    response = logged_client.delete(f'/cart/{purchase.pk}/')
    assert response.status_code == 204
    assert Purchase.objects.count() == 0


@pytest.mark.django_db
def test_purchase_create(user, logged_client):
    cart = factories.CartFactory(user=user)
    product = ProductFactory(name="Test name")
    payload = {
        'product': product.pk,
        'size': 33,
        'quantity': 5
    }

    response = logged_client.post(f'/cart/', data=payload)
    assert response.status_code == 201
    assert Purchase.objects.filter(cart=cart).count()== 1

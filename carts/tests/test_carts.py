import pytest

from products.tests.factories import ProductFactory, ProductSizeFactory

from ..models import Purchase
from . import factories


@pytest.mark.django_db
def test_purchase_list(user, logged_client):
    cart = factories.CartFactory(user=user)
    factories.PurchaseFactory.create_batch(cart=cart, size=10)
    response = logged_client.get("/cart/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 10


@pytest.mark.django_db
def test_purchase_destroy(user, logged_client):
    cart = factories.CartFactory(user=user)
    purchase = factories.PurchaseFactory(cart=cart)

    response = logged_client.delete(f"/cart/{purchase.pk}/")
    assert response.status_code == 204
    assert Purchase.objects.count() == 0


@pytest.mark.django_db
def test_purchase_create(user, logged_client):
    cart = factories.CartFactory(user=user)
    product = ProductFactory(name="Test name")
    product_size = ProductSizeFactory(size=33)
    product.sizes.add(product_size)
    payload = {"product": product.pk, "size": 33, "quantity": 5}
    # breakpoint()
    response = logged_client.post("/cart/", data=payload)
    assert response.status_code == 201
    assert Purchase.objects.filter(cart=cart).count() == 1


@pytest.mark.django_db
def test_purchase_patch(user, logged_client):
    cart = factories.CartFactory(user=user)
    purchase = factories.PurchaseFactory(
        size=5,
        quantity=2,
        cart=cart,
    )
    purchase.product.sizes.add(ProductSizeFactory(size=5))
    purchase.product.sizes.add(ProductSizeFactory(size=10))
    product_id = purchase.product_id
    payload = {
        "size": 10,
        "quantity": 4,
    }

    response = logged_client.patch(f"/cart/{purchase.pk}/", data=payload)
    assert response.status_code == 200
    purchase.refresh_from_db()
    assert purchase.size == 10
    assert purchase.quantity == 4
    assert purchase.product_id == product_id
    assert Purchase.objects.filter(cart=cart).count() == 1


@pytest.mark.django_db
def test_purchase_put(user, logged_client):
    cart = factories.CartFactory(user=user)
    purchase = factories.PurchaseFactory(
        size=5,
        quantity=2,
        cart=cart,
    )
    purchase.product.sizes.add(ProductSizeFactory(size=5))
    product_id = purchase.product_id
    payload = {
        "product": purchase.product_id,
        "size": 5,
        "quantity": 4,
    }

    response = logged_client.put(f"/cart/{purchase.pk}/", data=payload)
    assert response.status_code == 200
    purchase.refresh_from_db()
    assert purchase.size == 5
    assert purchase.quantity == 4
    assert purchase.product_id == product_id
    assert Purchase.objects.filter(cart=cart).count() == 1

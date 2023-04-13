import pytest

from . import factories


@pytest.mark.django_db
def test_product_list(logged_client):
    """Test"""
    for _ in range(10):
        product = factories.ProductFactory(price=10)
        product.sizes.add(factories.ProductSizeFactory())
    response = logged_client.get("/product/")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 10


@pytest.mark.django_db
def test_product_filter_by_product_type(logged_client):
    shoes = factories.ProductTypeFactory(name="shoes")
    pants = factories.ProductTypeFactory(name="pants")

    for product_type in [shoes] * 5 + [pants] * 5:
        factories.ProductFactory(price=10, product_type=product_type)

    response = logged_client.get("/product/?product_type=pants")
    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 5
    assert data["results"][0]["product_type"] == "pants"


@pytest.mark.django_db
def test_product_ordering_by_price_asc(logged_client):
    prices = [5, 3, 6, 7, 1]
    for price in prices:
        factories.ProductFactory(price=price)

    response = logged_client.get("/product/?ordering=price")
    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 5

    res_prices = [product["price"] for product in data["results"]]
    assert res_prices == sorted(prices)


@pytest.mark.django_db
def test_product_ordering_by_price_desc(logged_client):
    prices = [5, 3, 6, 7, 1]
    for price in prices:
        factories.ProductFactory(price=price)

    response = logged_client.get("/product/?ordering=-price")
    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 5

    res_prices = [product["price"] for product in data["results"]]
    assert res_prices == sorted(prices, reverse=True)


@pytest.mark.django_db
def test_product_ordering_by_name_asc(logged_client):
    names = ["aaa", "abb", "bbb", "fff", "zzz"]
    for name in names:
        factories.ProductFactory(price=10, name=name)

    response = logged_client.get("/product/?ordering=name")
    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 5

    res_names = [product["name"] for product in data["results"]]
    assert res_names == sorted(names)


@pytest.mark.django_db
def test_product_ordering_by_name_desc(logged_client):
    names = ["aaa", "abb", "bbb", "fff", "zzz"]
    for name in names:
        factories.ProductFactory(price=10, name=name)

    response = logged_client.get("/product/?ordering=-name")
    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 5

    res_names = [product["name"] for product in data["results"]]
    assert res_names == sorted(names, reverse=True)

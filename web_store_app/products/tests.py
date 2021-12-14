from django.test import TestCase, Client
import pytest


@pytest.mark.django_db
def test_product_page_get(client, example_product,
                      example_subcategory, example_product_subcategory_relation):  #product page test 1
    client = Client()
    response = client.get(f'/product/{example_product.id}/')
    assert response.status_code == 200
    product = response.context['product']
    assert product.name == 'Product 1'
    assert product.description == 'Product description 1'
    assert product.price == 100


@pytest.mark.django_db
def test_product_page_post(client, example_product,
                                  example_subcategory, example_product_subcategory_relation,
                                  example_website_user):  #product page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/product/{example_product.id}/', {'quantity': 1})
    assert response.status_code == 200
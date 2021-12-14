from django.test import TestCase, Client
import pytest


@pytest.mark.django_db
def test_home_page_get():  #homepage test 1
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_page_post():  #homepage test 2
    client = Client()
    response = client.post('/', {'key_word': 'a'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_page_get(client, example_category): #category page test 1
    client = Client()
    response = client.get(f'/category/{example_category.id}/')
    assert response.status_code == 200
    category = response.context['category']
    assert category.name == 'Category 1'
    assert category.description == 'Category description 1'


@pytest.mark.django_db
def test_category_page_post(client, example_category): #category page test 2
    client = Client()
    response = client.post(f'/category/{example_category.id}/', {'key_word': 'a'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_subcategory_page_get(client, example_subcategory, example_category, example_category_subcategory_relation): #subcategory page test 1
    client = Client()
    response = client.get(f'/subcategory/{example_subcategory.id}/')
    assert response.status_code == 200
    subcategory = response.context['subcategory']
    assert subcategory.name == 'Subcategory 1'
    assert subcategory.description == 'Subcategory description 1'


@pytest.mark.django_db
def test_subcategory_page_post(client, example_subcategory): #subcategory page test 2
    client = Client()
    response = client.post(f'/subcategory/{example_subcategory.id}/', {'key_word': 'a'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_shopping_cart_page_get(client, example_website_user): #shopping cart test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/shopping_cart/{example_website_user.id}/')
    assert response.status_code == 200
    assert response.context['products_summary'] == 0


@pytest.mark.django_db
def test_shopping_cart_page_post(client, example_website_user): #shopping cart test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/shopping_cart/{example_website_user.id}/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_shopping_cart_checkout_page_get(client, example_website_user): #shopping cart checkout test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/shopping_cart/{example_website_user.id}/checkout/')
    assert response.status_code == 200
    assert response.context['products_summary'] == 0


@pytest.mark.django_db
def test_shopping_cart_checkout_page_post(client, example_website_user): #shopping cart checkout test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/shopping_cart/{example_website_user.id}/checkout/', {'phone_number': 123456789})
    assert response.status_code == 302


@pytest.mark.django_db
def test_shopping_cart_remove_product_page_get(client, example_website_user, example_product, example_shopping_cart): #shopping cart remove product test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/shopping_cart/remove/{example_website_user.id}/{example_product.id}/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_shopping_cart_payment_page_get(client, example_product, example_website_user,
                                        example_shopping_cart, example_order): #shopping cart payment page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/shopping_cart/{example_website_user.id}/{example_order.id}/payment/')
    assert response.status_code == 200
    assert response.context['products_summary'] == 100


@pytest.mark.django_db
def test_shopping_cart_payment_page_post(client, example_product, example_website_user,
                                        example_shopping_cart, example_order): #shopping cart payment page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/shopping_cart/{example_website_user.id}/{example_order.id}/payment/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_shopping_cart_summary_page_get(client, example_product, example_website_user,
                                        example_shopping_cart, example_order): #shopping cart summary page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/shopping_cart/{example_website_user.id}/{example_order.id}/summary/')
    assert response.status_code == 200
    assert response.context['products_summary'] == 100
    assert response.context['order'] == example_order


@pytest.mark.django_db
def test_shopping_cart_summary_page_post(client, example_product, example_website_user,
                                        example_shopping_cart, example_order): #shopping cart summary page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/shopping_cart/{example_website_user.id}/{example_order.id}/summary/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_shopping_cart_success_page_get(client, example_product, example_website_user,
                                        example_shopping_cart, example_order): #shopping cart summary page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/shopping_cart/{example_website_user.id}/{example_order.id}/success/')
    assert response.status_code == 200
    assert response.context['order'] == example_order
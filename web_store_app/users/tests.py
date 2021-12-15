from django.test import TestCase, Client
import pytest
from users.models import WebsiteUser
from main.models import ProductOrder, Order
from datetime import datetime, date


@pytest.mark.django_db
def test_registration_page_get(client): #registration page test 1
    client = Client()
    response = client.get('/users/register/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_registration_page_post(client): #registration page test 2
    client = Client()
    response = client.post('/users/register/', {'username': 'test_user', 'password': 'test_password',
                                                 'first_name': 'test_first_name', 'last_name': 'test_last_name',
                                                 'email': 'test_email', 'address': 'test_address',
                                                 'phone_number': 123456789})
    assert response.status_code == 302
    assert WebsiteUser.objects.all().count() == 1
    assert WebsiteUser.objects.get(username='test_user')
    assert WebsiteUser.objects.get(first_name='test_first_name')
    assert WebsiteUser.objects.get(phone_number=123456789)


@pytest.mark.django_db
def test_login_page_get(client): #login page test 1
    client = Client()
    response = client.get('/users/login/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_page_post(client, example_website_user): #login page test 2
    client = Client()
    response = client.post('/users/login/', {'username': 'test_user', 'password': 'test_password'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_page_get(client): #logout page test 1
    client = Client()
    response = client.get('/users/logout/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_page_post(client): #logout page test 2
    client = Client()
    response = client.post('/users/logout/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_panel_page_get(client, example_website_user): #user panel page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/users/panel/{example_website_user.id}/')
    assert response.status_code == 200
    assert response.context['user'] == example_website_user


@pytest.mark.django_db
def test_user_panel_post(client, example_website_user): #user panel page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/users/panel/{example_website_user.id}/', {'key_word': 'a'})
    assert response.status_code == 200
    for product in response.context['product_results']:
        assert 'a' in product.name


@pytest.mark.django_db
def test_user_edit_page_get(client, example_website_user): #user edit page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/users/edit/{example_website_user.id}/')
    assert response.status_code == 200
    assert response.context['user'] == example_website_user


@pytest.mark.django_db
def test_user_edit_page_post(client, example_website_user): #user edit page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/users/edit/{example_website_user.id}/', {'username': 'put_username', 'password': 'put_password',
                                                                      'first_name': 'put_first_name', 'last_name': 'put_last_name',
                                                                      'email': 'put_email@gmail.com', 'phone_number': 111222333,
                                                                      'address': 'put_address'})
    assert response.status_code == 302
    user = WebsiteUser.objects.get(id=example_website_user.id)
    assert user.username == 'put_username'
    assert user.first_name == 'put_first_name'
    assert user.last_name == 'put_last_name'
    assert user.phone_number == 111222333


@pytest.mark.django_db
def test_user_orders_page_get(client, example_website_user,
                              example_order, example_product,
                              example_product_order_relation):  # user orders page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/users/panel/orders/{example_website_user.id}/')
    assert response.status_code == 200
    for order in response.context['orders']:
        assert order == Order.objects.get(user_id=example_website_user.id)
    for product_order in response.context['product_orders']:
        assert product_order == ProductOrder.objects.get(user_id=example_website_user.id)


@pytest.mark.django_db
def test_user_orders_page_post(client, example_website_user): #user orders page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/users/panel/orders/{example_website_user.id}/', {'key_word': 'a'})
    assert response.status_code == 200
    for product in response.context['product_results']:
        assert 'a' in product.name


@pytest.mark.django_db
def test_password_reset_page_get(client): #password reset page test 1
    client = Client()
    response = client.get(f'/users/password_reset/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_password_reset_page_post(client, example_website_user): #password reset page test 2
    client = Client()
    response = client.post(f'/users/password_reset/', {'email': 'test_email@test.com', 'password': 'reset_password'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_wallet_refill_page_get(client, example_website_user): #user wallet refill page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/users/wallet/{example_website_user.id}/refill/')
    assert response.status_code == 200
    user = WebsiteUser.objects.get(id=example_website_user.id)
    assert user.wallet == 500


@pytest.mark.django_db
def test_user_wallet_refill_page_post(client, example_website_user): #user wallet refill page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/users/wallet/{example_website_user.id}/refill/', {'amount': 500})
    assert response.status_code == 302
    user = WebsiteUser.objects.get(id=example_website_user.id)
    assert user.wallet == 1000


@pytest.mark.django_db
def test_user_wallet_withdraw_page_get(client, example_website_user): #user wallet withdraw page test 1
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.get(f'/users/wallet/{example_website_user.id}/withdraw/')
    assert response.status_code == 200
    user = WebsiteUser.objects.get(id=example_website_user.id)
    assert user.wallet == 500


@pytest.mark.django_db
def test_user_wallet_withdraw_page_post(client, example_website_user): #user wallet withdraw page test 2
    client = Client()
    client.login(username='test_user', password='test_password')
    response = client.post(f'/users/wallet/{example_website_user.id}/withdraw/', {'amount': '500'})
    assert response.status_code == 302
    user = WebsiteUser.objects.get(id=example_website_user.id)
    assert user.wallet == 0

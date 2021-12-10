from django.shortcuts import render
from django.views import View
from main.models import Category, ShoppingCart
from products.models import Product, SubCategoryProduct
from users.models import WebsiteUser
from django.http import HttpResponse
# Create your views here.


class ProductView(View):
    def get(self, request, product_id):
        last_viewed_product = ""
        # if request.session.get('last_viewed_product_id', False):
        #     last_viewed_product = request.session.get('last_viewed_product_id')
        # else:
        #     request.session['last_viewed_product_id'] = product_id
        #     last_viewed_product = request.session.get('last_viewed_product_id')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        product = Product.objects.get(id=product_id)
        shopping_cart = ShoppingCart.objects.all()
        subcategory = SubCategoryProduct.objects.filter(product_id=product_id)[0]
        response = render(request, 'product/product_details.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'product': product,
                                                                'shopping_cart_list': shopping_cart,
                                                                'subcategory': subcategory,
                                                                'last_viewed_product_id': last_viewed_product}
                      )
        if request.COOKIES.get('last_viewed_product_id'):
            last_viewed_product = request.COOKIES.get('last_viewed_product_id')
        else:
            response.set_cookie(key='last_viewed_product_id', value=product_id, max_age=10)
            last_viewed_product = request.COOKIES.get('last_viewed_product_id')
            return response
        return render(request, 'product/product_details.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'product': product,
                                                                'shopping_cart_list': shopping_cart,
                                                                'subcategory': subcategory,
                                                                'last_viewed_product_id': last_viewed_product}
                      )

    def post(self, request, product_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        user_id = request.POST.get('user_id')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id=product_id)
        user = WebsiteUser.objects.get(id=user_id)
        shopping_cart = ShoppingCart.objects.all()
        ShoppingCart.objects.create(product=product, user=user, quantity=quantity)
        return render(request, 'product/product_details.html', {'stringed_instruments': stringed_instruments,
                                                                'keyboard_instruments': keyboard_instruments,
                                                                'drums': drums,
                                                                'sound_system': sound_system,
                                                                'product': product,
                                                                'success_text': 'Product added to cart',
                                                                'shopping_cart_list': shopping_cart}
                      )
from django.shortcuts import render
from django.views import View
from main.models import Category, ShoppingCart
from products.models import Product
from users.models import WebsiteUser
# Create your views here.


class ProductView(View):
    def get(self, request, product_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        product = Product.objects.get(id=product_id)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'product/product_details.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'product': product,
                                                                'shopping_cart_list': shopping_cart}
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
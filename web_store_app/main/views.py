from django.shortcuts import render, redirect
from django.views import View
from .models import Category, SubCategory, CategorySubCategory, ShoppingCart, Order, ProductOrder
from products.models import Product
from datetime import date, timedelta
from users.models import WebsiteUser
# Create your views here.


class HomePageView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = SubCategory.objects.all()
        bestsellers_len = len(Product.objects.filter(is_bestseller=True))
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating').order_by('-rating')[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today()).order_by('-date_added')[0:3]
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/base.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'shopping_cart_list': shopping_cart}
                      )

    def post(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = SubCategory.objects.all()
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating')[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today()).order_by('-date_added')[0:3]
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/search_results.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'product_results': product_results,
                                                  'category_results': category_results,
                                                  'subcategory_results': subcategory_results,
                                                  'shopping_cart_list': shopping_cart}
                      )


class CategoryDetailsView(View):
    def get(self, request, category_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        subcategories = SubCategory.objects.filter(category_id=category_id)
        parent_category = CategorySubCategory.objects.filter(category_id=category_id)[0]
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/category_details.html', {'stringed_instruments': stringed_instruments,
                                                                'keyboard_instruments': keyboard_instruments,
                                                                'drums': drums,
                                                                'sound_system': sound_system,
                                                                'subcategories': subcategories,
                                                                'parent_category': parent_category,
                                                                'shopping_cart_list': shopping_cart}
                      )


class SubCategoryView(View):
    def get(self, request, subcategory_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        products = Product.objects.filter(subcategory_id=subcategory_id)
        parent_category = CategorySubCategory.objects.filter(subcategory_id=subcategory_id)[0]
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/subcategory_details.html', {'stringed_instruments': stringed_instruments,
                                                              'keyboard_instruments': keyboard_instruments,
                                                              'drums': drums,
                                                              'sound_system': sound_system,
                                                              'products': products,
                                                              'parent_category': parent_category,
                                                              'shopping_cart_list': shopping_cart})


class ContactView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/contact.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                                 'shopping_cart_list': shopping_cart})


class ShoppingCartView(View):
    def get(self, request, user_id):
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/')
        else:
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            return render(request, 'main/shoppingCart.html', {'stringed_instruments': stringed_instruments,
                                                              'keyboard_instruments': keyboard_instruments,
                                                              'drums': drums,
                                                              'sound_system': sound_system,
                                                              'shopping_cart_list': shopping_cart_list,
                                                              'products_summary': products_summary})
    def post(self, request, user_id):
        ShoppingCart.objects.all().delete()
        return redirect(f'/shopping_cart/{user_id}/')


class ShoppingCartCheckoutView(View):
    def get(self, request, user_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
        products_summary = sum(product.product.price*product.quantity for product in shopping_cart_list)
        return render(request, 'main/shoppingCart_checkout.html', {'stringed_instruments': stringed_instruments,
                                                          'keyboard_instruments': keyboard_instruments,
                                                          'drums': drums,
                                                          'sound_system': sound_system,
                                                          'shopping_cart_list': shopping_cart_list,
                                                          'products_summary': products_summary})
    def post(self, request, user_id):
        post_shipping_type = request.POST.get('shipping_type')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        shipping_type = 1
        if post_shipping_type == 'pickup_in_person':
            shipping_type = 1
        elif post_shipping_type == 'home_shipping':
            shipping_type = 2

        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)

        product_id = 0
        for product in shopping_cart_list:
            product_id = product.product.id
        quantity = 0
        for product_quantity in shopping_cart_list:
            quantity = product_quantity.quantity
        product = Product.objects.get(id=product_id)
        user = WebsiteUser.objects.get(id=user_id)
        order = Order.objects.create(shipping_type=shipping_type, user=user, phone_number=phone_number, address=address)

        ProductOrder.objects.create(order=order, product=product, quantity=quantity, user_id=user_id)

        return redirect(f'/shopping_cart/{user_id}/{order.id}/payment/')


class ShoppingCartRemoveProductView(View):
    def get(self, request, user_id, product_id):
        cart_item = ShoppingCart.objects.filter(user_id=user_id, product_id=product_id)[0]
        cart_item.delete()
        return redirect(f'/shopping_cart/{user_id}/')


class ShoppingCartPaymentView(View):
    def get(self, request, user_id, order_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
        products_summary = sum(product.product.price*product.quantity for product in shopping_cart_list)
        order = Order.objects.get(id=order_id)
        if order.shipping_type == 2:
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)-15
        else:
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)

        return render(request, 'main/shoppingCart_payment.html', {'stringed_instruments': stringed_instruments,
                                                          'keyboard_instruments': keyboard_instruments,
                                                          'drums': drums,
                                                          'sound_system': sound_system,
                                                          'shopping_cart_list': shopping_cart_list,
                                                          'products_summary': products_summary,
                                                          'order': order})

    def post(self, request, user_id, order_id):
        post_payment_type = request.POST.get('payment_type')
        payment_type = 1
        if post_payment_type == 'cash':
            payment_type = 1
        elif post_payment_type == 'credit_card':
            payment_type = 2
        elif post_payment_type == 'bank_transfer':
            payment_type = 3

        order = Order.objects.get(id=order_id)
        order.payment_type = payment_type
        order.save()
        return redirect(f'/shopping_cart/{user_id}/{order_id}/summary/')


class ShoppingCartSummaryView(View):
    def get(self, request, user_id, order_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
        products_summary = sum(product.product.price*product.quantity for product in shopping_cart_list)
        order = Order.objects.get(id=order_id)
        if order.shipping_type == 2:
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)+15
        else:
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
        return render(request, 'main/shoppingCart_summary.html', {'stringed_instruments': stringed_instruments,
                                                          'keyboard_instruments': keyboard_instruments,
                                                          'drums': drums,
                                                          'sound_system': sound_system,
                                                          'shopping_cart_list': shopping_cart_list,
                                                          'products_summary': products_summary,
                                                          'order': order})
    def post(self, request, user_id, order_id):
        return redirect(f'/shopping_cart/{user_id}/{order_id}/success/')


class ShoppingCartSuccessView(View):
    def get(self, request, user_id, order_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart = ShoppingCart.objects.filter(user_id=user_id)
        shopping_cart.delete()
        return render(request, 'main/shoppingCart_success.html', {'stringed_instruments': stringed_instruments,
                                                          'keyboard_instruments': keyboard_instruments,
                                                          'drums': drums,
                                                          'sound_system': sound_system})
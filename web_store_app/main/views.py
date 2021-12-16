from django.shortcuts import render, redirect
from django.views import View
from .models import Category, SubCategory, CategorySubCategory, ShoppingCart, Order, ProductOrder, Complaint, Newsletter
from products.models import Product
from datetime import date, timedelta
from users.models import WebsiteUser
from django.core.mail import send_mail

class HomePageView(View):
    def get(self, request):
        """
        Displays the application's home page
        :param request:
        :return home page html:
        """
        welcome_text = ', welcome!'
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating')[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today()).order_by('-date_added')[0:3]
        shopping_cart = ShoppingCart.objects.all()
        response = render(request, 'main/base.html', {'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'shopping_cart_list': shopping_cart,
                                                      'welcome_text': welcome_text,
                                                      'all_subcategories': all_subcategories}
                      )
        if request.COOKIES.get(f'welcome{request.user.id}'):
            welcome_text = ', welcome back!'
        else:
            response.set_cookie(key=f'welcome{request.user.id}', value='Welcome', max_age=86400)
            return response
        return render(request, 'main/base.html', {'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'all_subcategories': all_subcategories,
                                                  'shopping_cart_list': shopping_cart,
                                                  'welcome_text': welcome_text}
                      )

    def post(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating')[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today()).order_by('-date_added')[0:3]
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/search_results.html', {'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'all_subcategories': all_subcategories,
                                                  'product_results': product_results,
                                                  'category_results': category_results,
                                                  'subcategory_results': subcategory_results,
                                                  'shopping_cart_list': shopping_cart}
                      )


class CategoryDetailsView(View):
    def get(self, request, category_id):
        """
        Displays a specific category with it's details
        :param request:
        :param category_id:
        :return category details page:
        """
        category = Category.objects.get(id=category_id)
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        subcategories = SubCategory.objects.filter(category_id=category_id)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/category_details.html', {'all_categories': all_categories,
                                                              'all_subcategories': all_subcategories,
                                                              'category': category,
                                                                'subcategories': subcategories,
                                                                'shopping_cart_list': shopping_cart}
                      )

    def post(self, request, category_id):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating')[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today()).order_by('-date_added')[0:3]
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/search_results.html', {'bestsellers': bestsellers,
                                                            'added_recently': added_recently,
                                                            'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                            'product_results': product_results,
                                                            'category_results': category_results,
                                                            'subcategory_results': subcategory_results,
                                                            'shopping_cart_list': shopping_cart}
                      )


class SubCategoryView(View):
    def get(self, request, subcategory_id):
        """
        Displays a specific sub category with it's details
        :param request:
        :param subcategory_id:
        :return sub category details page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        products = Product.objects.filter(subcategory_id=subcategory_id)
        parent_category = CategorySubCategory.objects.filter(subcategory_id=subcategory_id)[0]
        subcategory = SubCategory.objects.get(id=subcategory_id)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/subcategory_details.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                              'products': products,
                                                              'parent_category': parent_category,
                                                                 'subcategory': subcategory,
                                                              'shopping_cart_list': shopping_cart})

    def post(self, request, subcategory_id):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating')[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today()).order_by('-date_added')[0:3]
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/search_results.html', {'bestsellers': bestsellers,
                                                            'added_recently': added_recently,
                                                            'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                            'product_results': product_results,
                                                            'category_results': category_results,
                                                            'subcategory_results': subcategory_results,
                                                            'shopping_cart_list': shopping_cart}
                      )


class ShoppingCartView(View):
    def get(self, request, user_id):
        """
        Displays user's shopping cart
        :param request:
        :param user_id:
        :return shopping cart page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            return render(request, 'main/shoppingCart2.html', {'all_categories': all_categories,
                                                              'all_subcategories': all_subcategories,
                                                              'shopping_cart_list': shopping_cart_list,
                                                              'products_summary': products_summary})
    def post(self, request, user_id):
        ShoppingCart.objects.filter(user_id=user_id).delete()
        return redirect(f'/shopping_cart/{user_id}/')


class ShoppingCartCheckoutView(View):
    def get(self, request, user_id):
        """
        Displays user's shopping cart checkout page. (with information about the chosen products and price amount)
        :param request:
        :param user_id:
        :return shopping cart checkout page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/checkout/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            if request.GET.get('discount_code'):
                discount_code = request.GET.get('discount_code')
                if discount_code == 'NEWSLETTER':
                    products_summary = products_summary - products_summary*0.20
            return render(request, 'main/shoppingCart_checkout.html', {'all_categories': all_categories,
                                                                       'all_subcategories': all_subcategories,
                                                                       'shopping_cart_list': shopping_cart_list,
                                                                       'products_summary': products_summary})

    def post(self, request, user_id):
        post_shipping_type = request.POST.get('shipping_type')
        phone_number = request.POST.get('phone_number')
        if len(phone_number) > 9:
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            return render(request, 'main/shoppingCart_checkout.html', {'shopping_cart_list': shopping_cart_list,
                                                                       'products_summary': products_summary,
                                                                       'error_text': 'Phone number can not have more than 9 digits'})
        address = request.POST.get('address')
        shipping_type = 1
        if post_shipping_type == 'pickup_in_person':
            shipping_type = 1
        elif post_shipping_type == 'home_shipping':
            shipping_type = 2

        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)

        user = WebsiteUser.objects.get(id=user_id)
        order = ""
        if request.GET.get('discount_code'):
            order = Order.objects.create(shipping_type=shipping_type, user=user, phone_number=phone_number,
                                         address=address, discount_code=request.GET.get('discount_code'))
        else:
            order = Order.objects.create(shipping_type=shipping_type, user=user, phone_number=phone_number,
                                         address=address)

        for shopping_cart_item in shopping_cart_list:
            product_id = shopping_cart_item.product.id
            product = Product.objects.get(id=product_id)
            ProductOrder.objects.create(order=order, product=product, quantity=shopping_cart_item.quantity, user=user)

        return redirect(f'/shopping_cart/{user_id}/{order.id}/payment/')


class ShoppingCartRemoveProductView(View):
    def get(self, request, user_id, product_id):
        """
        A blank page for the purpose of removing a product from the shopping cart
        :param request:
        :param user_id:
        :param product_id:
        :return redirect to shopping cart page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/remove/{request.user.id}/{product_id}/')
        else:
            cart_item = ShoppingCart.objects.filter(user_id=user_id, product_id=product_id)[0]
            cart_item.delete()
            return redirect(f'/shopping_cart/{user_id}/')


class ShoppingCartPaymentView(View):
    def get(self, request, user_id, order_id):
        """
        Displays information about the payment options from which user has to choose
        :param request:
        :param user_id:
        :param order_id:
        :return shopping cart payment page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/{order_id}/payment/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            order = Order.objects.get(id=order_id)

            return render(request, 'main/shoppingCart_payment.html', {'all_categories': all_categories,
                                                                      'all_subcategories': all_subcategories,
                                                                      'shopping_cart_list': shopping_cart_list,
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
        elif post_payment_type == 'wallet':
            payment_type = 4

        order = Order.objects.get(id=order_id)
        order.payment_type = payment_type
        order.save()
        return redirect(f'/shopping_cart/{user_id}/{order_id}/summary/')


class ShoppingCartSummaryView(View):
    def get(self, request, user_id, order_id):
        """
        Displays a list of information about the products chosen by user
        :param request:
        :param user_id:
        :param order_id:
        :return shopping cart summary page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/{order_id}/summary/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            order = Order.objects.get(id=order_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            final_summary = products_summary
            if order.shipping_type == 2 and len([shopping_cart.quantity for shopping_cart in shopping_cart_list]) < 3:
                if order.discount_code == 'NEWSLETTER':
                    final_summary = (products_summary - (products_summary * 0.20))+15
                    order.amount_paid = final_summary
                    order.save()
                else:
                    final_summary = products_summary + 15
                    order.amount_paid = final_summary
                    order.save()
            elif order.shipping_type == 2 and len([shopping_cart.quantity for shopping_cart in shopping_cart_list]) >= 3:
                if order.discount_code == 'NEWSLETTER':
                    final_summary = (products_summary - (products_summary * 0.20))
                    order.amount_paid = final_summary
                    order.save()
                else:
                    final_summary = products_summary
                    order.amount_paid = final_summary
                    order.save()
            elif order.shipping_type == 1 and order.discount_code == 'NEWSLETTER':
                final_summary = products_summary - (products_summary * 0.20)
                order.amount_paid = final_summary
                order.save()

            return render(request, 'main/shoppingCart_summary.html', {'all_categories': all_categories,
                                                                      'all_subcategories': all_subcategories,
                                                                      'shopping_cart_list': shopping_cart_list,
                                                                      'products_summary': final_summary,
                                                                      'order': order})

    def post(self, request, user_id, order_id):
        order = Order.objects.get(id=order_id)
        if order.payment_type == 4:
            user = WebsiteUser.objects.get(id=user_id)
            user.wallet -= int(request.POST.get('amount_paid'))
            if user.wallet < 0:
                shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
                products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
                order = Order.objects.get(id=order_id)
                if order.shipping_type == 2:
                    products_summary = sum(
                        product.product.price * product.quantity for product in shopping_cart_list) + 15
                else:
                    products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
                return render(request, 'main/shoppingCart_summary.html', {'shopping_cart_list': shopping_cart_list,
                                                                          'products_summary': products_summary,
                                                                          'order': order,
                                                                          'error_text': 'You dont have enough money in your wallet!'})
            else:
                user.save()
                return redirect(f'/shopping_cart/{user_id}/{order_id}/success/')
        else:
            return redirect(f'/shopping_cart/{user_id}/{order_id}/success/')


class ShoppingCartSuccessView(View):
    def get(self, request, user_id, order_id):
        """
        Displays information, that user has successfully finished the order and bought the chosen products
        :param request:
        :param user_id:
        :param order_id:
        :return shopping cart success page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/{order_id}/success/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            shopping_cart = ShoppingCart.objects.filter(user_id=user_id)
            shopping_cart.delete()
            return render(request, 'main/shoppingCart_success.html', {'all_categories': all_categories,
                                                                      'all_subcategories': all_subcategories})


class NewsletterView(View):
    def get(self, request):
        """
        Displays a form allowing user to sign in to newsletter
        :param request:
        :return newsletter page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/newsletter.html', {'all_categories': all_categories,
                                                        'all_subcategories': all_subcategories,
                                                        'shopping_cart_list': shopping_cart})

    def post(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        shopping_cart = ShoppingCart.objects.all()
        # if Newsletter.objects.get(user_id=request.user.id):
        #     return render(request, 'main/newsletter.html', {'all_categories': all_categories,
        #                                                     'all_subcategories': all_subcategories,
        #                                                     'shopping_cart_list': shopping_cart,
        #                                                     'error_text': 'You are already signed to your newsletter'})
        email = request.POST.get('email')
        send_mail(subject='Music Store Newsletter',
                  message='Thank you for joining to our newsletter, here is your -20% discount code: NEWSLETTER',
                  from_email='hillchar77@gmail.com',
                  recipient_list=[email])
        Newsletter.objects.create(user_id=request.user.id)
        return render(request, 'main/newsletter.html', {'all_categories': all_categories,
                                                        'all_subcategories': all_subcategories,
                                                        'shopping_cart_list': shopping_cart,
                                                        'success_text': 'Email sent.'
                                                                        ' Check your inbox for further details'})


class ComplaintView(View):
    def get(self, request):
        """
        Displays a form, allowing user to write a complaint
        :return complaint page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'main/complaint.html', {'all_categories': all_categories,
                                                        'all_subcategories': all_subcategories,
                                                        'shopping_cart_list': shopping_cart})

    def post(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        shopping_cart = ShoppingCart.objects.all()
        if request.POST.get('subject') and request.POST.get('content'):
            subject = request.POST.get('subject')
            content = request.POST.get('content')
            Complaint.objects.create(user_id=request.user.id, subject=subject, content=content)
            return render(request, 'main/complaint.html', {'all_categories': all_categories,
                                                           'all_subcategories': all_subcategories,
                                                           'shopping_cart_list': shopping_cart,
                                                           'success_text': 'Complaint sent'})

        else:
            return render(request, 'main/complaint.html', {'all_categories': all_categories,
                                                           'all_subcategories': all_subcategories,
                                                           'shopping_cart_list': shopping_cart,
                                                           'error_text': 'You must define a subject and content'})

from django.shortcuts import render, redirect
from django.views import View
from .models import Category, SubCategory, CategorySubCategory,\
                    ShoppingCart, Order, \
                    ProductOrder, Complaint, \
                    Newsletter, DiscountCode, DiscountCodeUsage
from products.models import Product
from users.models import WebsiteUser
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

all_categories = Category.objects.all()
all_subcategories = SubCategory.objects.all().order_by('name')
# from datetime import date, timedelta
# added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
#                                         date_added__lte=date.today()).order_by('-date_added')[0:3]


class HomePageView(View):
    def get(self, request):
        """
        Displays the application's home page
        :param request:
        :return home page html:
        """
        bestsellers = Product.objects.filter(is_bestseller=True).order_by('-rating')[0:3]
        added_recently = Product.objects.all().order_by('-id')[0:3]
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        welcome_text = ', welcome!'
        last_viewed_products = ""
        cleared_last_viewed_products = []
        displayed_last_viewed_products = []
        if request.session.get('last_viewed_products'):
            last_viewed_products = request.session.get('last_viewed_products').split(',')
            for product_id in last_viewed_products:
                if product_id:
                    if product_id in displayed_last_viewed_products:
                        pass
                    else:
                        displayed_last_viewed_products.append(product_id)
                        cleared_last_viewed_products.append(Product.objects.get(id=product_id))

        response = render(request, 'main/index.html', {'bestsellers': bestsellers,
                                                       'added_recently': added_recently,
                                                       'all_categories': all_categories,
                                                       'shopping_cart_list': shopping_cart_list,
                                                       'welcome_text': welcome_text,
                                                       'all_subcategories': all_subcategories,
                                                       'cleared_last_viewed_products': cleared_last_viewed_products[::-1][0:3]
                                                       }
                      )
        if request.COOKIES.get(f'welcome{request.user.id}'):
            welcome_text = ', welcome back!'
        else:
            response.set_cookie(key=f'welcome{request.user.id}', value='Welcome', max_age=86400)
            return response

        return response

    def post(self, request):
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        return render(request, 'main/search_results.html', {'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                            'product_results': product_results,
                                                            'category_results': category_results,
                                                            'subcategory_results': subcategory_results,
                                                            'shopping_cart_list': shopping_cart_list}
                      )


class CategoryDetailsView(View):
    def get(self, request, category_id):
        """
        Displays a specific category with it's details
        :param request:
        :param category_id:
        :return category details page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        category = Category.objects.get(id=category_id)
        subcategories = SubCategory.objects.filter(category_id=category_id)
        return render(request, 'main/category_details.html', {'all_categories': all_categories,
                                                              'all_subcategories': all_subcategories,
                                                              'category': category,
                                                              'subcategories': subcategories,
                                                              'shopping_cart_list': shopping_cart_list}
                      )

    def post(self, request, category_id):
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        return render(request, 'main/search_results.html', {'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                            'product_results': product_results,
                                                            'category_results': category_results,
                                                            'subcategory_results': subcategory_results,
                                                            'shopping_cart_list': shopping_cart_list}
                      )


class SubCategoryView(View):
    def get(self, request, subcategory_id):
        """
        Displays a specific sub category with it's details
        :param request:
        :param subcategory_id:
        :return sub category details page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        products = Product.objects.filter(subcategory_id=subcategory_id)
        parent_category = CategorySubCategory.objects.filter(subcategory_id=subcategory_id)[0]
        subcategory = SubCategory.objects.get(id=subcategory_id)
        return render(request, 'main/subcategory_details.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'products': products,
                                                                 'parent_category': parent_category,
                                                                 'subcategory': subcategory,
                                                                 'shopping_cart_list': shopping_cart_list})

    def post(self, request, subcategory_id):
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        return render(request, 'main/search_results.html', {'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                            'product_results': product_results,
                                                            'category_results': category_results,
                                                            'subcategory_results': subcategory_results,
                                                            'shopping_cart_list': shopping_cart_list}
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
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            return render(request, 'main/shoppingCart.html', {'all_categories': all_categories,
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
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            if request.GET.get('discount_code'):
                try:
                    discount_code = DiscountCode.objects.get(name=request.GET.get('discount_code'))
                except ObjectDoesNotExist:
                    messages.error(request, 'Discount code does not exist!')
                    return redirect(f'/shopping_cart/{request.user.id}/checkout/')
                try:
                    DiscountCodeUsage.objects.get(discount_code=discount_code, user=request.user)
                    messages.error(request, 'You already used this discount code!')
                    return redirect(f'/shopping_cart/{request.user.id}/checkout/')
                except ObjectDoesNotExist:
                    products_summary = products_summary - products_summary * discount_code.discount_percent / 100
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
                                                                       'error_text':
                                                                           'Phone number cannot have more than 9 digits'})
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
            try:
                discount_code = DiscountCode.objects.get(name=request.GET.get('discount_code'))
            except ObjectDoesNotExist:
                messages.error(request, 'Discount code does not exist!')
                return redirect(f'/shopping_cart/{request.user.id}/checkout/')
            try:
                DiscountCodeUsage.objects.get(discount_code=discount_code, user=request.user)
                messages.error(request, 'You already used this discount code!')
                return redirect(f'/shopping_cart/{request.user.id}/checkout/')
            except ObjectDoesNotExist:
                order = Order.objects.create(shipping_type=shipping_type, user=user, phone_number=phone_number,
                                             address=address, discount_code=discount_code)
                DiscountCodeUsage.objects.create(discount_code=discount_code, user=request.user)
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
        (automatically redirects back to shopping cart page)
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
        Displays a list of information about the order made by user
        :param request:
        :param user_id:
        :param order_id:
        :return shopping cart summary page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/shopping_cart/{request.user.id}/{order_id}/summary/')
        else:
            shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
            order = Order.objects.get(id=order_id)
            products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
            final_summary = products_summary
            if order.shipping_type == 2 and len([shopping_cart.quantity for shopping_cart in shopping_cart_list]) < 3:
                if order.discount_code:
                    final_summary = (products_summary - (products_summary * (order.discount_code.discount_percent/100)))+15
                    order.amount_paid = final_summary
                    order.save()
                else:
                    final_summary = products_summary + 15
                    order.amount_paid = final_summary
                    order.save()
            elif order.shipping_type == 2 and len([shopping_cart.quantity for shopping_cart in shopping_cart_list]) >= 3:
                if order.discount_code:
                    final_summary = (products_summary - (products_summary * (order.discount_code.discount_percent/100)))
                    order.amount_paid = final_summary
                    order.save()
                else:
                    final_summary = products_summary
                    order.amount_paid = final_summary
                    order.save()
            elif order.shipping_type == 1:
                if order.discount_code:
                    final_summary = products_summary - (products_summary * (order.discount_code.discount_percent/100))
                    order.amount_paid = final_summary
                    order.save()
                else:
                    final_summary = products_summary
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
            user.wallet -= float(request.POST.get('amount_paid'))
            if user.wallet < 0:
                messages.error(request, f"You have insufficient funds in your wallet! "
                                        f"<a href='/shopping_cart/{request.user.id}/{order_id}/payment/'><b>Go back to payment details</b></a>")
                return redirect(f'/shopping_cart/{request.user.id}/{order_id}/summary/')
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
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        return render(request, 'main/newsletter.html', {'all_categories': all_categories,
                                                        'all_subcategories': all_subcategories,
                                                        'shopping_cart_list': shopping_cart_list})

    def post(self, request):
        email = request.POST.get('email')
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        try:
            Newsletter.objects.get(email=email)
            messages.error(request, 'This e-mail is already signed to our newsletter!')
            return redirect('/newsletter/')
        except ObjectDoesNotExist:
            send_mail(subject='Newsletter',
                      message='Thank you for joining to our newsletter, here is your -20% discount code: NEWSLETTER',
                      from_email='hillchar77@gmail.com',
                      recipient_list=[email])
            Newsletter.objects.create(email=email)
            return render(request, 'main/newsletter.html', {'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                            'shopping_cart_list': shopping_cart_list,
                                                            'success_text': 'Email sent.'
                                                                            ' Check your inbox for further details'})


class ComplaintView(View):
    def get(self, request):
        """
        Displays a form, allowing user to write a complaint
        :return complaint page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        return render(request, 'main/complaint.html', {'all_categories': all_categories,
                                                       'all_subcategories': all_subcategories,
                                                       'shopping_cart_list': shopping_cart_list})

    def post(self, request):
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        if request.POST.get('subject') and request.POST.get('content'):
            subject = request.POST.get('subject')
            content = request.POST.get('content')
            Complaint.objects.create(user_id=request.user.id, subject=subject, content=content)
            return render(request, 'main/complaint.html', {'all_categories': all_categories,
                                                           'all_subcategories': all_subcategories,
                                                           'shopping_cart_list': shopping_cart_list,
                                                           'success_text': 'Complaint sent'})

        else:
            return render(request, 'main/complaint.html', {'all_categories': all_categories,
                                                           'all_subcategories': all_subcategories,
                                                           'shopping_cart_list': shopping_cart_list,
                                                           'error_text': 'You must define a subject and content'})

from django.shortcuts import render, redirect
from django.views import View
from products.models import Product
from datetime import date, timedelta
from main.models import Category, Order, ProductOrder, SubCategory, ShoppingCart
from users.models import WebsiteUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


class RegistrationView(View):
    def get(self, request):
        """
        Displays a registration form, allowing a new user to make an account
        :param request:
        :return registration form page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        return render(request, 'users/registration_form.html', {'all_categories': all_categories,
                                                                'all_subcategories': all_subcategories
                                                                })
    def post(self, request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = ""
        if request.POST.get('address'):
            address = request.POST.get('address')
        phone_number = 0
        if request.POST.get('phone_number'):
            phone_number = request.POST.get('phone_number')
        user = WebsiteUser.objects.create(username=username, first_name=first_name,
                            last_name=last_name, email=email,
                                          phone_number=phone_number, address=address)
        user.set_password(password)
        user.save()
        return redirect('/users/login/')


class LoginView(View):
    def get(self, request):
        """
        Displays a login form, allowing a user that already has an account to log in
        :param request:
        :return login form page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        return render(request, 'users/login_form.html', {'all_categories': all_categories,
                                                         'all_subcategories': all_subcategories,
                                                         })

    def post(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/login_form.html', {'all_categories': all_categories,
                                                             'all_subcategories': all_subcategories,
                                                             'error_text': 'Wrong username or password, try again'})


class LogoutView(View):
    def get(self, request):
        """
        Displays a prompt to make sure that user want's to log out
        :param request:
        :return logout form page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        return render(request, 'users/logout_form.html', {'all_categories': all_categories,
                                                          'all_subcategories': all_subcategories,
                                                          })

    def post(self, request):
        logout(request)
        return redirect('/')


class UserPanelView(View):
    def get(self, request, user_id):
        """
        Displays information about the logged user credentials, including the address, phone number etc.
        :param request:
        :param user_id:
        :return user panel page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/panel/{request.user.id}/')
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        user = WebsiteUser.objects.get(id=user_id)
        shopping_cart = ShoppingCart.objects.all()
        return render(request, 'users/userpanel.html', {'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                        'user': user,
                                                        'shopping_cart_list':shopping_cart
                                                            })

    def post(self, request, user_id):
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


class UserPanelEditView(View):
    def get(self, request, user_id):
        """
        Displays a form allowing the logged user to change his credentials
        :param request:
        :param user_id:
        :return user panel edit page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/edit/{request.user.id}/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            user = WebsiteUser.objects.get(id=user_id)
            shopping_cart = ShoppingCart.objects.all()
            return render(request, 'users/userpanel_edit.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'user': user,
                                                                 'shopping_cart_list':shopping_cart})
    def post(self, request, user_id):
        try:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            user = WebsiteUser.objects.get(id=user_id)
            if password != "":
                user.set_password(password)
            else:
                all_categories = Category.objects.all()
                all_subcategories = SubCategory.objects.all().order_by('name')
                user = WebsiteUser.objects.get(id=user_id)
                return render(request, 'users/userpanel_edit.html', {'all_categories': all_categories,
                                                                     'all_subcategories': all_subcategories,
                                                                     'user': user,
                                                                     'error_text': 'You have to type a password'})
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone_number
            user.address = address
            user.save()
            return redirect('/users/login/')
        except Exception:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            user = WebsiteUser.objects.get(id=user_id)
            return render(request, 'users/userpanel_edit.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'user': user,
                                                                 'error_text': "Something went wrong"})


class PasswordResetView(View):
    def get(self, request):
        """
        Displays a password reset form, allowing a user that has forgotten his password, to set a  new one
        :param request:
        :return password reset page:
        """
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        return render(request, 'users/password_reset.html', {'all_categories': all_categories,
                                                             'all_subcategories': all_subcategories,
                                                             })
    def post(self, request):
        try:
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = WebsiteUser.objects.get(email=email)
            user.set_password(password)
            user.save()
            return redirect('/users/login/')
        except Exception:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            return render(request, 'users/password_reset.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'error_text': "Something went wrong"})


class UserPanelOrdersView(View):
    def get(self, request, user_id):
        """
        Displays a list of orders made by the logged user
        :param request:
        :param user_id:
        :return user panel orders page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/panel/orders/{request.user.id}/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id).order_by('-id')
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            shopping_cart = ShoppingCart.objects.all()
            return render(request, 'users/userpanel_orders.html', {'user': user,
                                                                   'orders': orders,
                                                                   'all_categories': all_categories,
                                                                   'all_subcategories': all_subcategories,
                                                                   'product_orders': product_orders,
                                                                   'shopping_cart_list': shopping_cart})

    def post(self, request, user_id):
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


class UserPanelWalletRefillView(View):
    def get(self, request, user_id):
        """
        Displays a form allowing the logged user to refill his wallet
        :param request:
        :param user_id:
        :return user panel wallet refill page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/wallet/{request.user.id}/refill/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            user = WebsiteUser.objects.get(id=user_id)
            wallet = user.wallet
            shopping_cart = ShoppingCart.objects.all()
            return render(request, 'users/userpanel_wallet_refill.html', {'all_categories': all_categories,
                                                                          'all_subcategories': all_subcategories,
                                                                          'user': user,
                                                                          'orders': orders,
                                                                          'product_orders': product_orders,
                                                                          'wallet': wallet,
                                                                          'shopping_cart_list': shopping_cart})

    def post(self, request, user_id):
        amount = request.POST.get('amount')
        user = WebsiteUser.objects.get(id=user_id)
        user.wallet += int(amount)
        user.save()
        return redirect(f'/users/panel/{user_id}/')


class UserPanelWalletWithdrawView(View):
    def get(self, request, user_id):
        """
        Displays a form allowing the logged user to withdraw from his wallet
        :param request:
        :param user_id:
        :return user panel withdraw page:
        """
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/wallet/{request.user.id}/withdraw/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            user = WebsiteUser.objects.get(id=user_id)
            wallet = user.wallet
            shopping_cart = ShoppingCart.objects.all()
            return render(request, 'users/userpanel_wallet_withdraw.html', {'all_categories': all_categories,
                                                                            'all_subcategories': all_subcategories,
                                                                            'user': user,
                                                                            'orders': orders,
                                                                            'product_orders': product_orders,
                                                                            'wallet': wallet,
                                                                            'shopping_cart_list': shopping_cart})

    def post(self, request, user_id):
        amount = request.POST.get('amount')
        user = WebsiteUser.objects.get(id=user_id)
        user.wallet -= int(amount)
        if user.wallet < 0:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            user = WebsiteUser.objects.get(id=user_id)
            wallet = user.wallet

            return render(request, 'users/userpanel_wallet_withdraw.html',
                          {'all_categories': all_categories,
                           'all_subcategories': all_subcategories,
                           'user': user,
                           'orders': orders,
                           'product_orders': product_orders,
                           'wallet': wallet,
                           'error_text': f'You can only withdraw {user.wallet}$'})
        else:
            user.save()
        return redirect(f'/users/panel/{user_id}/')
from django.shortcuts import render, redirect
from django.views import View
from products.models import Product
from main.models import Category, Order, ProductOrder, SubCategory, ShoppingCart
from users.models import WebsiteUser
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from users.forms import RegistrationForm
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

all_categories = Category.objects.all()
all_subcategories = SubCategory.objects.all().order_by('name')


class RegistrationView(View):
    def get(self, request):
        """
        Displays a registration form, allowing a new user to make an account
        :param request:
        :return registration form page:
        """
        form = RegistrationForm
        return render(request, 'users/registration_form.html', {'all_categories': all_categories,
                                                                'all_subcategories': all_subcategories,
                                                                'form': form
                                                                })

    def post(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        form = RegistrationForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password2']:
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            address = ""
            if form.cleaned_data['address']:
                address = form.cleaned_data['address']
            phone_number = 0
            if form.cleaned_data['phone_number']:
                phone_number = form.cleaned_data['phone_number']
            user = WebsiteUser.objects.create(username=username, first_name=first_name,
                                              last_name=last_name, email=email,
                                              phone_number=phone_number, address=address)
            user.set_password(password)
            user.save()
            return redirect('/users/login/')
        elif form.data['password'] and form.data['password2'] and form.data['password'] != form.data['password2']:
            form.add_error('password2', 'Passwords do not match')
            return render(request, 'users/registration_form.html', {'form': form,
                                                                    'all_categories': all_categories,
                                                                    'all_subcategories': all_subcategories})
        else:
            return render(request, 'users/registration_form.html', {'form': form,
                                                                    'all_categories': all_categories,
                                                                    'all_subcategories': all_subcategories
                                                                    })


class LoginView(View):
    def get(self, request):
        """
        Displays a login form, allowing a user that already has an account to log in
        :param request:
        :return login form page:
        """
        return render(request, 'users/login_form.html', {'all_categories': all_categories,
                                                         'all_subcategories': all_subcategories,
                                                         })

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password, try again')
            return redirect('/users/login/')


class LogoutView(View):
    def get(self, request):
        """
        Displays a prompt to make sure that user want's to log out
        :param request:
        :return logout form page:
        """
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
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/panel/{request.user.id}/')
        user = WebsiteUser.objects.get(id=user_id)
        return render(request, 'users/userpanel.html', {'all_categories': all_categories,
                                                        'all_subcategories': all_subcategories,
                                                        'user': user,
                                                        'shopping_cart_list': shopping_cart_list
                                                        })

    def post(self, request, user_id):
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


class UserPanelEditView(View):
    def get(self, request, user_id):
        """
        Displays a form allowing the logged user to change his credentials
        :param request:
        :param user_id:
        :return user panel edit page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/edit/{request.user.id}/')
        else:
            user = WebsiteUser.objects.get(id=user_id)
            return render(request, 'users/userpanel_edit.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'user': user,
                                                                 'shopping_cart_list': shopping_cart_list})

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
                user = authenticate(username=request.user.username, password=password)
                if user is None:
                    messages.error(request, 'Wrong password!')
                    return redirect(f'/users/edit/{request.user.id}/')

            else:
                messages.error(request, 'You have to type your password')
                return redirect(f'/users/edit/{request.user.id}/')
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone_number
            user.address = address
            user.save()
            login(request, user)
            messages.success(request, 'Data successfully updated!')
            return redirect(f'/users/edit/{request.user.id}/')

        except Exception:
            messages.success(request, 'Something went wrong!')
            return redirect(f'/users/edit/{request.user.id}/')


class PasswordResetView(View):
    def get(self, request):
        """
        Displays a password reset form, allowing a user that has forgotten his password, to make a request for a new one
        :param request:
        :return password reset page:
        """
        return render(request, 'users/password_reset.html', {'all_categories': all_categories,
                                                             'all_subcategories': all_subcategories,
                                                             })

    def post(self, request):
            email = request.POST.get('email')
            user = ""
            try:
                user = WebsiteUser.objects.get(email=email)
            except ObjectDoesNotExist:
                messages.error(request, "Incorrect e-mail")
                return redirect('/users/password_reset/')
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            domain = get_current_site(request).domain
            link = reverse('password-reset-verification', kwargs={'uidb64': uidb64, 'token': token})
            email_subject = 'Password reset'
            activation_url = f'http://{domain}{link}'
            email_body = f'Hello {user}, your password reset link:  {activation_url}'
            send_mail(
                email_subject,
                email_body,
                'noreply@noreply.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Check your e-mail inbox for further details')
            return render(request, 'users/password_reset.html', {'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories
                                                                 })


class PasswordResetVerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = WebsiteUser.objects.get(id=id)
            if not token_generator.check_token(user, token):
                messages.error(request, 'Password has already been changed')
                return redirect('login-page')
            return render(request, 'users/new_password_form.html', {'all_categories': all_categories,
                                                                    'all_subcategories': all_subcategories})
        except ObjectDoesNotExist:
            messages.error(request, 'Incorrect link or password is already changed')
            return redirect('login-page')

    def post(self, request, uidb64, token):
        id = force_str(urlsafe_base64_decode(uidb64))
        user = WebsiteUser.objects.get(id=id)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords mismatch')
            return render(request, 'users/new_password_form.html', {'all_categories': all_categories,
                                                                    'all_subcategories': all_subcategories,})

        user.set_password(password1)
        user.save()

        messages.success(request, 'Password changed successfully')
        return redirect('login-page')


class UserPanelOrdersView(View):
    def get(self, request, user_id):
        """
        Displays a list of orders made by the logged user
        :param request:
        :param user_id:
        :return user panel orders page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/panel/orders/{request.user.id}/')
        else:
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id).order_by('-id')
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            return render(request, 'users/userpanel_orders.html', {'user': user,
                                                                   'orders': orders,
                                                                   'all_categories': all_categories,
                                                                   'all_subcategories': all_subcategories,
                                                                   'product_orders': product_orders,
                                                                   'shopping_cart_list': shopping_cart_list})

    def post(self, request, user_id):
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


class UserPanelWalletRefillView(View):
    def get(self, request, user_id):
        """
        Displays a form allowing the logged user to refill his wallet
        :param request:
        :param user_id:
        :return user panel wallet refill page:
        """
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/wallet/{request.user.id}/refill/')
        else:
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            wallet = user.wallet
            return render(request, 'users/userpanel_wallet_refill.html', {'all_categories': all_categories,
                                                                          'all_subcategories': all_subcategories,
                                                                          'user': user,
                                                                          'orders': orders,
                                                                          'product_orders': product_orders,
                                                                          'wallet': wallet,
                                                                          'shopping_cart_list': shopping_cart_list})

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
        shopping_cart_list = ShoppingCart.objects.filter(user_id=request.user.id)
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/wallet/{request.user.id}/withdraw/')
        else:
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            wallet = user.wallet
            return render(request, 'users/userpanel_wallet_withdraw.html', {'all_categories': all_categories,
                                                                            'all_subcategories': all_subcategories,
                                                                            'user': user,
                                                                            'orders': orders,
                                                                            'product_orders': product_orders,
                                                                            'wallet': wallet,
                                                                            'shopping_cart_list': shopping_cart_list})

    def post(self, request, user_id):
        amount = request.POST.get('amount')
        user = WebsiteUser.objects.get(id=user_id)
        user.wallet -= int(amount)
        if user.wallet < 0:
            messages.error(request, f"You can't withdraw more than {request.user.wallet}$")
            return redirect(f'/users/wallet/{request.user.id}/withdraw/')
        else:
            user.save()
        return redirect(f'/users/panel/{user_id}/')


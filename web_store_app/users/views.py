from django.shortcuts import render, redirect
from django.views import View
from main.models import Category, Order, ProductOrder, SubCategory
from users.models import WebsiteUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.


class RegistrationView(View):
    def get(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/registration_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                                'all_categories': all_categories,
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
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/login_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                         'all_categories': all_categories,
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
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            return render(request, 'users/login_form.html', {'stringed_instruments': stringed_instruments,
                                                             'keyboard_instruments': keyboard_instruments,
                                                             'drums': drums,
                                                             'sound_system': sound_system,
                                                             'all_categories': all_categories,
                                                             'all_subcategories': all_subcategories,
                                                             'error_text': 'Wrong username or password, try again'})


class LogoutView(View):
    def get(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/logout_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                          'all_categories': all_categories,
                                                          'all_subcategories': all_subcategories,
                                                          })

    def post(self, request):
        logout(request)
        return redirect('/')


class UserPanelView(View):
    def get(self, request, user_id):
        logged_user_id = request.user.id
        if user_id != logged_user_id:
             return redirect(f'/users/panel/{request.user.id}/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            user = WebsiteUser.objects.get(id=user_id)
            return render(request, 'users/userpanel.html', {'stringed_instruments': stringed_instruments,
                                                        'keyboard_instruments': keyboard_instruments,
                                                        'drums': drums,
                                                        'sound_system': sound_system,
                                                            'all_categories': all_categories,
                                                            'all_subcategories': all_subcategories,
                                                        'user': user,
                                                            })


class UserPanelEditView(View):
    def get(self, request, user_id):
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/edit/{request.user.id}/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            user = WebsiteUser.objects.get(id=user_id)
            return render(request, 'users/userpanel_edit.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                                 'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'user': user})
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
                stringed_instruments = Category.objects.get(id=1)
                keyboard_instruments = Category.objects.get(id=2)
                drums = Category.objects.get(id=3)
                sound_system = Category.objects.get(id=4)
                user = WebsiteUser.objects.get(id=user_id)
                return render(request, 'users/userpanel_edit.html', {'stringed_instruments': stringed_instruments,
                                                                     'keyboard_instruments': keyboard_instruments,
                                                                     'drums': drums,
                                                                     'sound_system': sound_system,
                                                                     'all_categories': all_categories,
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
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            user = WebsiteUser.objects.get(id=user_id)
            return render(request, 'users/userpanel_edit.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                                 'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'user': user,
                                                                 'error_text': "Something went wrong"})



class PasswordResetView(View):
    def get(self, request):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/password_reset.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                             'all_categories': all_categories,
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
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            return render(request, 'users/password_reset.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                                 'all_categories': all_categories,
                                                                 'all_subcategories': all_subcategories,
                                                                 'error_text': "Something went wrong"})


class UserPanelOrdersView(View):
    def get(self, request, user_id):
        logged_user_id = request.user.id
        if user_id != logged_user_id:
            return redirect(f'/users/panel/orders/{request.user.id}/')
        else:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            return render(request, 'users/userpanel_orders.html', {'stringed_instruments': stringed_instruments,
                                                                   'keyboard_instruments': keyboard_instruments,
                                                                   'drums': drums,
                                                                   'sound_system': sound_system,
                                                                   'user': user,
                                                                   'orders': orders,
                                                                   'all_categories': all_categories,
                                                                   'all_subcategories': all_subcategories,
                                                                   'product_orders': product_orders})

class UserPanelWalletRefillView(View):
    def get(self, request, user_id):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        user = WebsiteUser.objects.get(id=user_id)
        orders = Order.objects.filter(user_id=user_id)
        product_orders = ProductOrder.objects.filter(user_id=user_id)
        user = WebsiteUser.objects.get(id=user_id)
        wallet = user.wallet

        return render(request, 'users/userpanel_wallet_refill.html', {'stringed_instruments': stringed_instruments,
                                                               'keyboard_instruments': keyboard_instruments,
                                                               'drums': drums,
                                                               'sound_system': sound_system,
                                                                      'all_categories': all_categories,
                                                                      'all_subcategories': all_subcategories,
                                                               'user': user,
                                                               'orders': orders,
                                                               'product_orders': product_orders,
                                                               'wallet': wallet})

    def post(self, request, user_id):
        amount = request.POST.get('amount')
        user = WebsiteUser.objects.get(id=user_id)
        user.wallet += int(amount)
        user.save()
        return redirect(f'/users/panel/{user_id}/')


class UserPanelWalletWithdrawView(View):
    def get(self, request, user_id):
        all_categories = Category.objects.all()
        all_subcategories = SubCategory.objects.all().order_by('name')
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        user = WebsiteUser.objects.get(id=user_id)
        orders = Order.objects.filter(user_id=user_id)
        product_orders = ProductOrder.objects.filter(user_id=user_id)
        user = WebsiteUser.objects.get(id=user_id)
        wallet = user.wallet

        return render(request, 'users/userpanel_wallet_withdraw.html', {'stringed_instruments': stringed_instruments,
                                                               'keyboard_instruments': keyboard_instruments,
                                                               'drums': drums,
                                                               'sound_system': sound_system,
                                                                        'all_categories': all_categories,
                                                                        'all_subcategories': all_subcategories,
                                                               'user': user,
                                                               'orders': orders,
                                                               'product_orders': product_orders,
                                                               'wallet': wallet})

    def post(self, request, user_id):
        amount = request.POST.get('amount')
        user = WebsiteUser.objects.get(id=user_id)
        user.wallet -= int(amount)
        if user.wallet < 0:
            all_categories = Category.objects.all()
            all_subcategories = SubCategory.objects.all().order_by('name')
            stringed_instruments = Category.objects.get(id=1)
            keyboard_instruments = Category.objects.get(id=2)
            drums = Category.objects.get(id=3)
            sound_system = Category.objects.get(id=4)
            user = WebsiteUser.objects.get(id=user_id)
            orders = Order.objects.filter(user_id=user_id)
            product_orders = ProductOrder.objects.filter(user_id=user_id)
            user = WebsiteUser.objects.get(id=user_id)
            wallet = user.wallet

            return render(request, 'users/userpanel_wallet_withdraw.html',
                          {'stringed_instruments': stringed_instruments,
                           'keyboard_instruments': keyboard_instruments,
                           'drums': drums,
                           'sound_system': sound_system,
                           'all_categories': all_categories,
                           'all_subcategories': all_subcategories,
                           'user': user,
                           'orders': orders,
                           'product_orders': product_orders,
                           'wallet': wallet,
                           'error_text': f'You can only withdraw {user.wallet}$'})
        else:
            user.save()
        return redirect(f'/users/panel/{user_id}/')
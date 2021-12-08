from django.shortcuts import render, redirect
from django.views import View
from main.models import Category
from users.models import WebsiteUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.


class RegistrationView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/registration_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system})
    def post(self, request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = WebsiteUser.objects.create(username=username, first_name=first_name,
                            last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return redirect('/users/login/')


class LoginView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/login_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Something went wrong!!')


class LogoutView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'users/logout_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system})

    def post(self, request):
        logout(request)
        return redirect('/')


class UserPanelView(View):
    def get(self, request, user_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        user = WebsiteUser.objects.get(id=user_id)
        return render(request, 'users/userpanel_form.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system,
                                                                 'user':user})
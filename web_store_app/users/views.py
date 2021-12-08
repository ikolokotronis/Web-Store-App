from django.shortcuts import render, redirect
from django.views import View
from main.models import Category
from users.models import WebsiteUser
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
        WebsiteUser.objects.create(username=username, first_name=first_name,
                            last_name=last_name, email=email,
                            password=password)
        return redirect('/')
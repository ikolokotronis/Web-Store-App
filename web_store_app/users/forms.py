from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='E-mail')
    phone_number = forms.IntegerField(label='Phone number(optional)', required=None)
    address = forms.CharField(label='Address(optional)', required=None)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

from django import forms
from django.forms import ModelForm
from seller.models import *
from store.models import *
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

class sellerform(ModelForm):
    class Meta:
        model = Seller
        fields = ['email' , 'phone' , 'office_address']

class ProductAdd(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
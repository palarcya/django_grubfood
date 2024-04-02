from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Customer, Food, Order

#Add Food Form
class FoodForm(ModelForm):
    class Meta:
        model = Food #FoodForm is working with the Food model
        fields = ['name', 'description', 'price'] #input fields for the form

#Add Customer Form
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'address', 'city']

#Add Order Form
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['paymentmode', 'quantity', 'food', 'customer']

#Add registration form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


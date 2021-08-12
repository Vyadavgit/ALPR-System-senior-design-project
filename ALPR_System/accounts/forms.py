from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import *

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff']

    def clean_email(self, *args, **kwargs):
        user_input = self.cleaned_data.get("email")
        return user_input

class CustomerForm(ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter first "
                                                                                             "name"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter last name"}))
    gender = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter your gender: "
                                                                                         "Male/Female/Other"}))
    birth_date = forms.DateField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter your birth date: "
                                                                                             "yyyy-mm-dd"}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter email address"}))

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class vehicleRegistrationForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ['owner', 'status']

class AddVehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__' # ['License_Plate', 'Make', 'Status', 'Update', 'Remove']


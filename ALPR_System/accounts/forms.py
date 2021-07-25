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

class AddResidentForm(ModelForm):
    class Meta:
        model = Resident
        fields = ['name', 'apartment_unit']

class AddVehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__' # ['License_Plate', 'Make', 'Status', 'Update', 'Remove']


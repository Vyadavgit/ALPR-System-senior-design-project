from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date
from phone_field import PhoneField

from django.db.models.deletion import CASCADE

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=25, blank=True)
    birth_date = models.DateField(null=True)
    # profile_picture = models.ImageField(default="profile_null.png", null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        if self.first_name and self.last_name:
            identity = (self.first_name + " " + self.last_name)
        else:
            identity = str(self.id)
        return identity

class Resident(models.Model):
    name = models.CharField(max_length=50, null=True)
    apartment_unit = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    

# class Vehicle(models.Model): 

#     STATUS = (
#             ('Pending', 'Pending'),
#             ('Approved', 'Approved'),
#             )

#     license_plate = models.CharField(max_length=50, null=True)
#     make = models.CharField(max_length=50, null=True)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)

#     def __str__(self):
#         return self.name
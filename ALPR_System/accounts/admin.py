from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Parkingspace)


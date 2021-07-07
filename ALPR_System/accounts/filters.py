import django_filters

from .models import *

class NameFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'
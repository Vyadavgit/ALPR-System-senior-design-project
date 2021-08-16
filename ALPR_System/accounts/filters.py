import django_filters

from .models import *

class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = ['owner', 'license_plate', 'status']
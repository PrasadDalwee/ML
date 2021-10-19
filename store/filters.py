import django_filters
from django_filters import DateFilter,RangeFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    class Meta:
        model = Product
        fields = ['name' , 'digital' , 'price']

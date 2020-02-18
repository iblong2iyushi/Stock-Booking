from rest_framework import serializers
from .models import Stocks, Customers


class StocksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Stocks
        fields = ['stock_name']

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Customers
        fields = ['customer_name']



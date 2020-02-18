from django.shortcuts import render
from rest_framework import viewsets
from .models import Stocks, Customers
from .serializers import StocksSerializer, CustomersSerializer
# Create your views here.

class StocksViewSet(viewsets.ModelViewSet):
    queryset=Stocks.objects.all()
    serializer_class= StocksSerializer

class CustomersViewSet(viewsets.ModelViewSet):
    queryset=Customers.objects.all()
    serializer_class= CustomersSerializer 

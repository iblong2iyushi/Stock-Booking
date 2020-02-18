from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customers,Bookings,Stocks
from django.conf import settings

# Create your views here.

def display(request):
    return HttpResponse("Welcome to the stock booking site")

def list_customer(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    result = ''
    for cus in Customers.objects.all():
        result += str(cus)
        result += "<br>"
    return HttpResponse(result)

def add_customer(request, name):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    # now save it in database
    c = Customers(customer_name=name)
    c.save()
    return HttpResponse("Done")

def update_customer(request, old_name, new_name):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    c = Customers.objects.get(customer_name=old_name)
    c.customer_name = new_name
    c.save()
    return HttpResponse("Done")
    

def delete_customer(request, name):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    c = Customers.objects.get(customer_name=name)
    c.delete()
    return HttpResponse("Done")

def list_stock(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    result = ''
    for stock in Stocks.objects.all():
        result += str(stock)
        result += "<br>"
    return HttpResponse(result)

def add_stock(request, name):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    s = Stocks(stock_name = name)
    s.save()
    return HttpResponse("Done")

def update_stock(request,old_name,new_name):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    s = Stocks.objects.get(stock_name = old_name)
    s.stock_name = new_name
    s.save()
    return HttpResponse("Done")

def delete_stock(request, name):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s'%(settings.LOGIN_URL, request.path))
    s = Stocks.objects.get(stock_name = name)
    s.delete()
    return HttpResponse("Done")


    

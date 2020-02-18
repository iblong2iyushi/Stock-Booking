from django.contrib import admin

# Register your models here.

from .models import Customers,Stocks,Bookings

admin.site.register(Customers)
admin.site.register(Stocks)
admin.site.register(Bookings)

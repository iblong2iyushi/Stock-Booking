from django.db import models

# Create your models here.

class Stocks(models.Model):
     stock_name = models.CharField(max_length = 200)

     def __str__(self):
         return self.stock_name

class Customers(models.Model):
    customer_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.customer_name

class Bookings(models.Model):
    sid = models.ForeignKey(Stocks,on_delete = models.CASCADE)
    cid = models.ForeignKey(Customers,on_delete = models.CASCADE)


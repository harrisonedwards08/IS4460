from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 15)

class Order(models.Model):
    customer = models.ForeignKey(to = Customer,on_delete = models.CASCADE)
    order_total = models.DecimalField(max_digits=7,decimal_places=2)
    notes = models.CharField(max_length=100,default='')
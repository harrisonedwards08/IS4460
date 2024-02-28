from django.db import models
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length = 100)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_items = models.IntegerField()
    order_date = models.DateField(default=timezone.now().date())



cust1 = Customer.objects.get(pk=2)
cust1.name
'Big Comp'
order1 = Order()
order1.customer = cust1
order1.total_price = 18.75
order1.total_items = 2
order1.save()
 
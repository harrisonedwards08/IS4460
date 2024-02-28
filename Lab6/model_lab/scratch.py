from customer.models import Customer
cust1 = Customer()

cust1.name = "ABC Comp"
cust1.save()
cust2 = Customer()
cust2.name = "Big Comp"
cust2.save()


Customer.objects.get(pk=1)
customer_one = Customer.objects.get(pk=1)
customer_one.name = "Harry's Upgraded Comp"
customer_one.save()
customer_one.delete





Customer.objects.create(name = "Red Team")
Customer.objects.create(name = "Blue Team")
Customer.objects.create(name = "Betas")
results = Customer.objects.filter(name__startswith=("Red"))
results.count()
results[0].name
'Red Team'

results2 = Customer.objects.filter(name__endswith=("Team"))

qs_all = Customer.objects.all()
qs_all.count()

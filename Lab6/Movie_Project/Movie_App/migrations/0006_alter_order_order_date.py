# Generated by Django 5.0.1 on 2024-03-03 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
    ]
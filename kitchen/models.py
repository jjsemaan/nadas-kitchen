from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    first_line_address = models.CharField(max_length=255)
    second_line_address = models.CharField(max_length=255)
    eir_code = models.CharField(max_length=255)

class MenuItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.BinaryField()

class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivery_status = models.CharField(max_length=255)
    paid = models.BooleanField()

class Receipt(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ['id']
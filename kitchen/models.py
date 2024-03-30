from django.db import models
from customer.models import Customer
from customer.models import MenuItem
# from django.contrib.auth.models import User

# STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Order(models.Model):
    # Define the Order model representing orders made by customers.
    order_id = models.BigAutoField(primary_key=True)  # Unique identifier for the order.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Reference to the customer placing the order.
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # Reference to the menu item ordered.
    delivery_date = models.DateField()  # Date of delivery for the order.
    delivery_time = models.TimeField()  # Time of delivery for the order.
    delivery_status = models.CharField(max_length=255)  # Status of the delivery.
    paid = models.BooleanField()  # Boolean indicating whether the order has been paid for.

class Receipt(models.Model):
    # Define the Receipt model representing receipts generated for orders.
    id = models.BigAutoField(primary_key=True)  # Unique identifier for the receipt.
    description = models.CharField(max_length=255)  # Description of the receipt.
    total = models.DecimalField(max_digits=8, decimal_places=2)  # Total amount on the receipt.

    class Meta:
        unique_together = ['id']  # Ensure uniqueness of the 'id' field across receipts.

from django.db import models
#from django.contrib.auth.models import User
from customer.models import Customer
from customer.models import MenuItem

# Create your models here.
class Order(models.Model):
    # Define the Order model representing orders made by customers.
    PAID_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    DELIVERY_STATUS_CHOICES = [
        ('PREPARING', 'Preparing'),
        ('DISPATCHED', 'Dispatched'),
        ('IN_TRANSIT', 'In-transit'),
        ('DELIVERED', 'Delivered'),
    ]

    HOUR_CHOICES = [(f"{hour:02d}:00", f"{hour:02d}:00") for hour in range(24)]

    order_id = models.BigAutoField(primary_key=True)  # Unique identifier for the order.
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Reference to the customer placing the order.
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # Reference to the menu item ordered.
    delivery_date = models.DateField()  # Date of delivery for the order.
    delivery_time = models.CharField(max_length=5, choices=HOUR_CHOICES)  # Choice field for delivery time.
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES)  # Updated field with choices
    paid = models.CharField(max_length=3, choices=PAID_CHOICES)  # Choice field for payment status.

class Receipt(models.Model):
    # Define the Receipt model representing receipts generated for orders.
    id = models.BigAutoField(primary_key=True)  # Unique identifier for the receipt.
    description = models.CharField(max_length=255)  # Description of the receipt.
    total = models.DecimalField(max_digits=8, decimal_places=2)  # Total amount on the receipt.

    class Meta:
        unique_together = ['id']  # Ensure uniqueness of the 'id' field across receipts.

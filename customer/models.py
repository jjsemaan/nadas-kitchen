from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

class Customer(models.Model):
    # Fields for customer information
    id = models.BigAutoField(primary_key=True)  # Unique identifier for the customer
    first_name = models.CharField(max_length=255)  # First name of the customer
    last_name = models.CharField(max_length=255)  # Last name of the customer
    email = models.EmailField(max_length=255, unique=True)  # Email address of the customer
    mobile_phone = models.CharField(max_length=10, default='', unique=True)  # Mobile number of the customer

    # Custom validation method
    def clean(self):
        # Check if the mobile number is a 10-digit integer starting with zero
        if not self.mobile_number.startswith('0') or not self.mobile_number.isdigit() or len(self.mobile_number) != 10:
            raise ValidationError("Mobile number must be a 10-digit integer starting with zero.")

    # String representation of the Customer object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MenuItem(models.Model):
    # Define the MenuItem model representing items in the menu.
    item_id = models.BigAutoField(primary_key=True)  # Unique identifier for the menu item.
    name = models.CharField(max_length=255)  # Name of the menu item.
    description = models.CharField(max_length=255)  # Description of the menu item.
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price of the menu item.
    quantity = models.IntegerField()  # Quantity of the menu item available.
    category = models.CharField(max_length=255)  # Category of the menu item.
    image = models.BinaryField()  # Image of the menu item stored as binary data.
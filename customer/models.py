from django.db import models

# Create your models here.
class Customer(models.Model):
    # Define the Customer model representing customers.
    id = models.BigAutoField(primary_key=True)  # Unique identifier for the customer.
    first_name = models.CharField(max_length=255)  # Name of the customer.
    last_name = models.CharField(max_length=255)  # Name of the customer.
    email = models.EmailField(max_length=255)  # Email address of the customer.
    first_line_address = models.CharField(max_length=255)  # First line of the customer's address.
    second_line_address = models.CharField(max_length=255)  # Second line of the customer's address.
    eir_code = models.CharField(max_length=255)  # Eircode of the customer's address.

class MenuItem(models.Model):
    # Define the MenuItem model representing items in the menu.
    item_id = models.BigAutoField(primary_key=True)  # Unique identifier for the menu item.
    name = models.CharField(max_length=255)  # Name of the menu item.
    description = models.CharField(max_length=255)  # Description of the menu item.
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price of the menu item.
    quantity = models.IntegerField()  # Quantity of the menu item available.
    category = models.CharField(max_length=255)  # Category of the menu item.
    image = models.BinaryField()  # Image of the menu item stored as binary data.
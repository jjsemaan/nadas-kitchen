from django.db import models

class Customer(models.Model):
    # Choices for country code selection
    COUNTRY_CHOICES = (
        ('IE', 'Ireland'),  # Ireland is the default choice
        # Add other country codes and names as needed
    )

    # Fields for customer information
    id = models.BigAutoField(primary_key=True)  # Unique identifier for the customer
    first_name = models.CharField(max_length=255)  # First name of the customer
    last_name = models.CharField(max_length=255)  # Last name of the customer
    email = models.EmailField(max_length=255)  # Email address of the customer
    country_code = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='IE')  # Country code of the customer
    mobile_number = models.CharField(max_length=10, default='')  # Mobile number of the customer

    # Address fields
    first_line_address = models.CharField(max_length=255)  # First line of the customer's address
    second_line_address = models.CharField(max_length=255, blank=True)  # Second line of the customer's address
    eir_code = models.CharField(max_length=255)  # Eircode of the customer's address

    # Custom validation method
    def clean(self):
        # Check if the selected country is Ireland
        if self.country_code != 'IE':
            raise ValidationError("We do not deliver outside Ireland.")

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
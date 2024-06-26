# Generated by Django 4.2.11 on 2024-03-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_alter_order_delivery_time_alter_order_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('PREPARING', 'Preparing'), ('DISPATCHED', 'Dispatched'), ('IN_TRANSIT', 'In-transit'), ('DELIVERED', 'Delivered')], max_length=20),
        ),
    ]

# Generated by Django 4.2.11 on 2024-03-30 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'unique_together': {('id',)},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.TimeField()),
                ('delivery_status', models.CharField(max_length=255)),
                ('paid', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.menuitem')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-31 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_order_id', models.CharField(max_length=100, unique=True)),
                ('payment_status', models.CharField(choices=[('initiated', 'Initiated'), ('successful', 'Successful'), ('failed', 'Failed')], default='initiated', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='order.order')),
            ],
        ),
    ]

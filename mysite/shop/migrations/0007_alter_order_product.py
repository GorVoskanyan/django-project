# Generated by Django 4.2.7 on 2023-11-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', to='shop.product'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-30 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0010_auto_20201001_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='items_in_cart',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='no_of_sales',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='total_sale_amount',
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_product_price_product_price_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_new',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]

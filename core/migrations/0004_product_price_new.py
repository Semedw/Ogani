# Generated by Django 4.2.4 on 2023-08-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_product_price_new_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_new',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.1.2 on 2024-11-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks_app', '0004_alter_category_options_cart_cartitem_cart_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
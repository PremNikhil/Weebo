# Generated by Django 3.2.5 on 2021-07-05 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_art_clothes_laptop_covers_mobile_covers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clothes',
            new_name='Clothing',
        ),
        migrations.RenameModel(
            old_name='Laptop_Covers',
            new_name='Laptop_Cover',
        ),
        migrations.RenameModel(
            old_name='Mobile_Covers',
            new_name='Mobile_Cover',
        ),
    ]
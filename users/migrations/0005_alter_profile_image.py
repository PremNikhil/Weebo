# Generated by Django 3.2.5 on 2021-07-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='def.jpg', upload_to='profile_pictures'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='def.JPG', upload_to='profile_pics'),
        ),
    ]

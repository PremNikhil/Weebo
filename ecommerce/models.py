
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image
from django.db.models.fields.files import ImageField
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title     


class Mobile_Cover(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='mobile_cover_pictures')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Laptop_Cover(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='laptop_cover_pictures')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Art(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='painting_cover_pictures')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




class Clothing(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    rating = models.FloatField(blank=True, null = True)
    quantity = models.IntegerField(blank=True)
    image=models.ImageField(default='default.jpg', upload_to='clothing_cover_pictures')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.decorators import login_required


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures', default='def.jpg')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path) 
         
        if img.height > 270 or img.width >270:
            output_size = (270,270)
            img.thumbnail(output_size)
            img.save(self.image.path)
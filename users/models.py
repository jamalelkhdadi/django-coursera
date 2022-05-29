from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    image = models.ImageField(default='coursera/user.png', upload_to='coursera/profile_pics/%y/%m/%d')

    def __str__(self):
        return f'{self.user.username} Profile'


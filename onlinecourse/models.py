from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from PIL import Image
from django.contrib.postgres.fields import ArrayField

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})



class Course(models.Model):

    name = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='coursera/portfolio_pics/%y/%m/%d')
    url = models.CharField(max_length=300)
    technologys = ArrayField(models.CharField(max_length=50), blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})



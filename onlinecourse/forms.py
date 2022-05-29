from django import forms
from .models import *

from django.contrib.postgres.fields import ArrayField

from django.forms import fields



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CourseForm(forms.ModelForm):
    technologys = ArrayField(forms.CharField(max_length=50, required=False))
    class Meta:
        model = Course
        fields = ['name', 'title', 'description', 'url', 'technologys', 'category', 'image']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


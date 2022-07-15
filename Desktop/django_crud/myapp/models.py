from unicodedata import name
from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length=200)
    bday = models.DateField()
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    hobby = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    address = models.TextField()

    def __str__(self):
        return self.name
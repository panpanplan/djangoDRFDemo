from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    pub_date = models.DateTimeField('date published')

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

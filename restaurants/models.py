from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    description = models.TextField()
    food_set = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Address(models.Model):
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address_line = models.CharField(max_length=100)


class Comment(models.Model):
    author = models.CharField(max_length=50)
    quality = models.FloatField(default=5,validators=[MaxValueValidator(5), MinValueValidator(0)])
    packaging = models.FloatField(default=5,validators=[MaxValueValidator(5), MinValueValidator(0)])
    delivery_time = models.FloatField(default=5,validators=[MaxValueValidator(5), MinValueValidator(0)])
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images')
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    average_rate = models.FloatField()




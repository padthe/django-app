from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=100)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    time = models.TimeField(max_length=100)


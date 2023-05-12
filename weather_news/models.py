from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    temperature = models.FloatField()
    #date = models.DateTimeField()

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

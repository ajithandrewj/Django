from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=20)
    hero=models.CharField(max_length=20)
    heroine=models.CharField(max_length=20)
    releasedDate=models.DateField()
    genre=models.CharField(max_length=10)
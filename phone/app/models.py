from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50)

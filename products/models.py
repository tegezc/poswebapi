from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    nip = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField()

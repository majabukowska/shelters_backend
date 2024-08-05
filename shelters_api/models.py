from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pets/')

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    needs = models.TextField()

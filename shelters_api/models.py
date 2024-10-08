from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    liked_pets = models.ManyToManyField('Pet', related_name='liked_by', blank=True)

    groups = models.ManyToManyField(Group, related_name='shelters_api_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='shelters_api_users', blank=True)

    @classmethod
    def create_superuser(cls):
        if not cls.objects.filter(username='admin').exists():
            cls.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpassword'
            )
            print("Superuser created.")

class Pet(models.Model):
    name = models.CharField(max_length=100, default="")
    species = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    is_liked = models.BooleanField(default=False)
    can_adopt = models.BooleanField(default=True)
    can_volunteer = models.BooleanField(default=True)
    image_data = models.TextField(blank=True, null=True)
    shelter = models.ForeignKey('Shelter', on_delete=models.CASCADE, related_name='pets')

    class Meta:
        unique_together = ('name', 'shelter')

class Shelter(models.Model):
    name = models.CharField(max_length=100, default="")
    address = models.TextField(unique=True)    
    needs = models.TextField(default="")
    website_link = models.URLField(default="", blank=True)
    news_link = models.URLField(default="", blank=True)
    x_coordinate = models.FloatField(default=0.0)
    y_coordinate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

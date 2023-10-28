from uuid import uuid4
from django.db import models
#from django.contrib.auth.models import AbstractUser

## TODO: Make this the right type of Model, either should be AbstractUser of a simple models.Model
class CustomUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=15,unique=True)
    # Add any other custom fields you need for your user model

    def __str__(self):
        return self.email

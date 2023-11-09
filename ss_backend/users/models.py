# users/models.py
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from users.manager import CustomUserManager  # Import your custom manager

class CustomUser(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)  # Explicitly define id field
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)

    objects = CustomUserManager()  # Use the custom manager

    def __str__(self):
        return self.email

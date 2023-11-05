from uuid import uuid4
from django.db import models
#from django.contrib.auth.models import AbstractUser

#TODO: Make this model according to Django users, currenlty this model represents a mock

class Users(models.Model):
    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15,unique=True)
    #TODO: following fields to be added accordingly for permissions
    """
    - is_staff
    - is_superuser
    - is_active
    - tier_user
    """


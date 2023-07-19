from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class Account(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]
    class Meta:
        unique_together = ('email','username')

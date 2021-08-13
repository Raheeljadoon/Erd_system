from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User_signup(AbstractBaseUser):

    email = models.EmailField(max_length=255,unique=True,)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
class User_login(AbstractBaseUser):

    email = models.EmailField(max_length=255,unique=True,)
    password = models.CharField(max_length=20)
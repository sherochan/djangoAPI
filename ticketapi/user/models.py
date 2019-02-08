from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):

    objects = CustomUserManager()

    def __str__(self):
        return self.email

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    # name = models.CharField(max_length=255,unique = True,default="")
    # email = models.EmailField(max_length= 254, unique = True)
    # created = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()
    # USERNAME_FIELD = 'name'

    # def save(self, *args, **kwargs):
    #     super(CustomUser, self).save(*args, **kwargs) # Call the real   save() method
    #
    # #
    def __str__(self):
        return self.email

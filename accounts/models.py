from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True,blank=True)
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.email
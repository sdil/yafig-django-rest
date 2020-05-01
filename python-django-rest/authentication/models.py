from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)
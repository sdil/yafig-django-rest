from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    status = models.CharField(blank=True, max_length=120)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    joined_at = models.DateTimeField(auto_now=True)

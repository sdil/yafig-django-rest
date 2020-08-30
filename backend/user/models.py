from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    status = models.CharField(default="PENDING", blank=True, max_length=120)
    description = models.CharField(blank=True, max_length=256)
    followers_count = models.IntegerField(default=0)
    posts_count= models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    joined_at = models.DateTimeField(auto_now=True)

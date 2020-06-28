from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    status = models.CharField(default="PENDING", blank=True, max_length=120)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    joined_at = models.DateTimeField(auto_now=True)

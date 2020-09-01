from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    status = models.CharField(default="PENDING", blank=True, max_length=120)
    description = models.CharField(blank=True, max_length=256)
    followers_count = models.IntegerField(default=0)
    posts_count= models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    joined_at = models.DateTimeField(auto_now=True)

class Relationship(models.Model):
    FRIEND = "Friend"
    BLOCKED = "Blocked"
    RELATIONSHIP_TYPE = [(FRIEND, "Friend"), (BLOCKED, "Blocked")]

    user1 = models.ForeignKey(User, related_name="actor", on_delete=models.DO_NOTHING)
    user2 = models.ForeignKey(User, related_name="target", on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=128, choices=RELATIONSHIP_TYPE, default=FRIEND)
    created_at = models.DateTimeField(auto_now=True)

from django.db import models
from user.models import User

class Post(models.Model):
    caption = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(blank=True, max_length=120)
    posted_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

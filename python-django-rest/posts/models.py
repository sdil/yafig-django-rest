from django.db import models


class Post(models.Model):
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

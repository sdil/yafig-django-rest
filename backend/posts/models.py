from uuid import uuid4

from django.db.models import JSONField
from django.db import models

from user.models import User


def upload_image_to(instance, filename):
    ext = filename.split(".")[-1]
    return f"{uuid4().hex}.{ext}"


class Post(models.Model):
    caption = models.TextField()
    status = models.CharField(blank=True, max_length=120)
    tags = JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="user", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    image = models.ImageField(upload_to=upload_image_to)

    @property
    def tags_indexing(self):
        """
        Tags for indexing.

        Used in Elasticsearch indexing.
        """
        return [tag for tag in self.tags]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    created_by = models.DateTimeField(auto_now_add=True)
    created_at = models.ForeignKey(
        User, on_delete=models.DO_NOTHING
    )

class Timeline(models.Model):
    # The order is by primary key because it's auto increment
    # This is not scalable
    user = models.ForeignKey(User, related_name="owner", on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name="post", on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)

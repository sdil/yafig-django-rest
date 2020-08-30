import logging

from rest_framework import serializers
from posts.models import Comment, Post, Timeline
from user.serializers import UserSerializer

logger = logging.getLogger(__name__)


class PostSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "image", "caption", "posted_by"]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "comment", "user")

class TimelineSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Timeline
        fields = ["post"]

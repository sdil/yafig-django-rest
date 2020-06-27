import logging

from rest_framework import serializers

from posts.models import Comment, Post

logger = logging.getLogger(__name__)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "comment")

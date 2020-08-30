import logging

from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from user.models import User
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class PostListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = PostSerializer
    # MultiPart handle files upload using Form Data format
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        """
        This view should return a list of all the posts
        for the currently authenticated user.
        """
        current_user = self.request.user
        return Post.objects.filter(posted_by=current_user)

    def perform_create(self, serializer):
        # Assign the owner of the image to the current user
        serializer.save(posted_by=self.request.user)

        # Increase the posts count of the image owner
        logger.info("increase the users posts_count number")
        self.request.user.posts_count += 1
        self.request.user.save()
        logger.info("done")



class CommentListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

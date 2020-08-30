import logging

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Comment, Post, Timeline
from .serializers import CommentSerializer, PostSerializer, TimelineSerializer
from user.models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


logger = logging.getLogger(__name__)


class TimelineList(ListAPIView):
    serializer_class = TimelineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return get_list_or_404(Timeline.objects.order_by("-order"), user=user)


class PostListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = PostSerializer
    # MultiPart handle files upload using Form Data format
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticatedOrReadOnly]

    # @method_decorator(cache_page(60*60*2))
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
        self.request.user.posts_count += 1
        self.request.user.save()

        # Index the image in elasticsearch

        # Asynchronously add this image to all his/her followers timeline


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the posts
        for the currently authenticated user.
        """
        return Post.objects.all()


class CommentListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

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
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .tasks import generate_thumbnail, publish_post_to_timelines
from .permission import IsOwnerOrReadOnly

logger = logging.getLogger(__name__)


class TimelineList(ListAPIView):
    serializer_class = TimelineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Timeline.objects.filter(user=user).order_by("-id")


class PostListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = PostSerializer
    # MultiPart handle files upload using Form Data format
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the posts
        for the currently authenticated user.
        """
        current_user = self.request.user
        return Post.objects.filter(created_by=current_user)

    def perform_create(self, serializer):
        """
        Document is automatically indexed in Elasticsearch
        using elasticsearch-dsl library
        """

        # Assign the owner of the image to the current user
        post = serializer.save(created_by=self.request.user)

        # Increase the posts count of the image owner
        self.request.user.posts_count += 1
        self.request.user.save()

        # Generate thumbnail
        generate_thumbnail.delay()

        # Asynchronously add this image to all his/her followers timeline
        publish_post_to_timelines.delay(self.request.user.id, post.id)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the posts
        for the currently authenticated user.
        """
        return Post.objects.all()

    def perform_update(self, serializer):
        serializer.save()

        # update elasticsearch index

    def perform_destroy(self, instance):
        instance.delete()

        # delete in all timelines


class Search(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        q = self.request.query_params.get("q")
        if q is not None:
            return search(q)
        return super().get_queryset()


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()


class CommentListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """

    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()

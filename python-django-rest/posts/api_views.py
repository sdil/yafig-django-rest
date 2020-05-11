from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
import logging
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class PostListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """
    serializer_class = PostSerializer
    # MultiPart handle files upload using Form Data format
    parser_classes = (MultiPartParser,)
    queryset = Post.objects.all()

class CommentListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

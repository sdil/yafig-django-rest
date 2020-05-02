from rest_framework.generics import ListCreateAPIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

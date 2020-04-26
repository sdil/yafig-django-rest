from rest_framework.generics import ListCreateAPIView

from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPI accepts both GET and POST request
    Refer here: https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
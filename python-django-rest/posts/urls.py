from django.urls import path
from .api_views import PostListCreateAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name = 'api-post-list'),
]
from django.urls import path
from .api_views import PostListCreateAPIView, CommentListCreateAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name = 'post-list-create'),
    path('<int:post_id>/comment/', CommentListCreateAPIView.as_view(), name = 'comment-list-create'),
]
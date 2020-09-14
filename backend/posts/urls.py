from django.urls import path

from .api_views import (
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    PostListCreateAPIView,
    PostRetrieveUpdateDestroyAPIView,
    TimelineList
)

urlpatterns = [
    path("", PostListCreateAPIView.as_view(), name="post-list-create"),
    path("timeline/", TimelineList.as_view(), name="timeline"),
    path("search", TimelineList.as_view(), name="search"),
    path(
        "<int:pk>/",
        PostRetrieveUpdateDestroyAPIView.as_view(),
        name="post-detail-update-delete",
    ),
    path(
        "<int:post_id>/comment/",
        CommentListCreateAPIView.as_view(),
        name="comment-list-create",
    ),
    path(
        "<int:post_id>/comment/<int:comment_id>",
        CommentRetrieveUpdateDestroyAPIView.as_view(),
        name="comment-detail-update-delete",
    ),
]

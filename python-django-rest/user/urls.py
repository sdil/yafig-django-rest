from django.urls import path
from user import api_views
from rest_framework import permissions

urlpatterns = [
    path('login/', api_views.TokenObtainPairView.as_view(), name='user_login'),
    path('register/', api_views.register, name="user-register"),
    path('<str:username>/', api_views.UserDetail.as_view(), name='get_user_detail'),
    # path('<str:username>/posts/', jwt_views.TokenObtainPairView.as_view(), name = 'user-post-list'),
    # path('follow/<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    # path('block/<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
]
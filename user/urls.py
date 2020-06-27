from django.urls import path
from rest_framework import permissions

from rest_framework_simplejwt import views as jwt_views
from user import api_views

urlpatterns = [
    path('', api_views.get_current_user, name="get-current-user"),
    path('login', api_views.TokenObtainPairView.as_view(), name='user-login'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='user-refresh-token'),
    path('register/', api_views.register, name="user-register"),
    path('<str:username>/', api_views.UserDetail.as_view(), name='get-user-detail'),
    path('<str:username>/posts/', api_views.UserPosts.as_view(), name = 'user-post-list'),
    # path('follow/<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    # path('block/<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
]

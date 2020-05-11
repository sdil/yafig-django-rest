from django.urls import path
from user import api_views
from rest_framework import permissions

urlpatterns = [
    path('', api_views.get_current_user, name="get-current-user"),
    path('login/', api_views.TokenObtainPairView.as_view(), name='user-login'),
    path('register/', api_views.register, name="user-register"),
    path('<str:username>/', api_views.UserDetail.as_view(), name='get-user-detail'),
    # path('<str:username>/posts/', jwt_views.TokenObtainPairView.as_view(), name = 'user-post-list'),
    # path('follow/<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    # path('block/<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
]
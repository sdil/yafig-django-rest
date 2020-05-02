from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('<str:username>/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
]
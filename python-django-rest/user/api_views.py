from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import Http404
from rest_framework import permissions
from drf_yasg.utils import swagger_serializer_method
from rest_framework.decorators import api_view, schema ,permission_classes
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import AutoSchema, ManualSchema
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class UserDetail(APIView):
    """
    get:
    Get current user. 
    This API resources use API View.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, username, format=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(user)
        return Response(serializer.data)

class CustomObtainTokenPairWithView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """
    Register a new user and return it's details
    """
    print(request.data)
    user = User.objects.create_user(request.data['username'], password=request.data['password'])
    return Response(UserSerializer(user).data)

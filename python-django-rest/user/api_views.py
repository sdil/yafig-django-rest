from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import Http404
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, schema ,permission_classes
from drf_yasg.openapi import IN_BODY, IN_PATH, Parameter, Schema, TYPE_STRING, TYPE_OBJECT

# Create your views here.
class UserDetail(APIView):
    """
    get:
    Get current user. 
    This API resources use API View.

    post:
    Update current user.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, username, format=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=UserSerializer,
        security=[]
    )
    def post(self, request, username, format=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(user)
        return Response(serializer.data)

class CustomObtainTokenPairWithView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

# More documentation here
# https://drf-yasg.readthedocs.io/en/stable/drf_yasg.html#drf_yasg.utils.swagger_auto_schema
# https://drf-yasg.readthedocs.io/en/stable/custom_spec.html#serializer-meta-nested-class
# https://drf-yasg.readthedocs.io/en/stable/drf_yasg.html#drf_yasg.openapi.Parameter
# https://github.com/axnsan12/drf-yasg/issues/280    
@swagger_auto_schema(
    method='post',
    operation_description="apiview post description override",
    request_body=Schema(
        type=TYPE_OBJECT,
        required=['username'],
        properties={
            'username': Schema(type=TYPE_STRING)
        },
    ),
    security=[]
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """
    Register a new user and return it's details
    """
    serializer_class = UserSerializer
    print(request.data)
    user = User.objects.create_user(request.data['username'], password=request.data['password'])
    return Response(UserSerializer(user).data)

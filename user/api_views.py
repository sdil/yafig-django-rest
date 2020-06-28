import logging

from django.http import Http404
from rest_framework.exceptions import PermissionDenied
from drf_yasg.openapi import (
    FORMAT_EMAIL,
    FORMAT_PASSWORD,
    IN_HEADER,
    TYPE_OBJECT,
    TYPE_STRING,
    Parameter,
    Schema,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import CustomTokenObtainPairSerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserDetail(APIView):
    """
    get:
    Get current user.
    This API resources use API View.

    post:
    Update current user.
    """

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get user details", responses={200: UserSerializer}
    )
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update user details",
        request_body=UserSerializer,
        responses={200: UserSerializer},
    )
    def post(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Delete user. The user can only delete himself.",
        request_body=UserSerializer,
        responses={200: UserSerializer},
    )
    def delete(self, request, username):
        # Only can delete yourself
        if request.user.username == username:
            user = get_object_or_404(User, pk=request.user.id)
            user.status = "DELETED"
            user.is_active = False
            user.save()
            return Response({"status": "OK"})
        else:
            raise PermissionDenied(
                {"message": "You do not have permission to delete this user"}
            )


class UserPosts(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get user's posts",
        responses={200: PostSerializer(many=True)},
    )
    def get(self, request, username):
        try:
            posts = Post.objects.filter(posted_by=username)
        except User.DoesNotExist:
            raise Http404
        serializer = PostSerializer(posts, many=True)
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
    method="post",
    operation_description="User registration",
    request_body=Schema(
        type=TYPE_OBJECT,
        required=["username", "password"],
        properties={
            "username": Schema(type=TYPE_STRING, format=FORMAT_EMAIL),
            "password": Schema(type=TYPE_STRING, format=FORMAT_PASSWORD),
        },
    ),
    responses={200: UserSerializer},
)
@api_view(["POST"])
@permission_classes(
    [permissions.AllowAny,]
)
def register(request):
    """
    Register a new user and return it's details
    """
    user = User.objects.create_user(
        request.data["username"], password=request.data["password"]
    )
    return Response(UserSerializer(user).data)


@swagger_auto_schema(
    method="get",
    operation_description="User authenticate",
    manual_parameters=[
        Parameter(
            "Authorization",
            IN_HEADER,
            description="JWT Token of current user",
            type=TYPE_STRING,
        )
    ],
    responses={200: UserSerializer},
)
@api_view(["GET"])
@permission_classes(
    [permissions.IsAuthenticated,]
)
def get_current_user(request):
    """
    Authenticate current user and return his/her details
    """
    current_user = UserSerializer(request.user)
    logger.info(f"Authenticating current user {request.user.username}")

    return Response(current_user.data)

"""yafig_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views
from rest_framework.schemas import get_schema_view as drf_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="YAFIG API Server",
        default_version='v1',
        description='Yet Another Free Instagram Clone API Server (Monolith)',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

drf_schema_view = drf_schema_view(
    title='YAFIG API',
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path("doc/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-redoc'),
    path('schema/', drf_schema_view),
    path('admin/', admin.site.urls),
    path("posts/", include("posts.urls")),
    path("users/", include('user.urls')),
]

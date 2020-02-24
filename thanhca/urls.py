"""thanhca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import (include, re_path, path)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Thanhca Admin API",
        default_version='v1',
        description="Api For Amin",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bboyadao@gmail.com"),
        license=openapi.License(name="Thanhca"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
)

api_docs = [
    re_path('api/docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('api/docs/swagger$', schema_view.with_ui('swagger',
                                                     cache_timeout=0), name='schema-swagger-ui'),
    re_path('api/docs/redoc/$', schema_view.with_ui('redoc',
                                                    cache_timeout=0), name='schema-redoc'),
]


api = [
    path('admin/', admin.site.urls),
]


urlpatterns = api + api_docs

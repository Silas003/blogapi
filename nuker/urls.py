from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('api/',include('blog_api.urls',namespace='blog_api')),
    path('api/user/',include('users.urls',namespace='users')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
     path('api/token/verify',TokenVerifyView.as_view(),name='token_verify'),
     path('docs/',include_docs_urls(title='Blog')),
    #   path('openapi', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …",
    #     version="1.0.0"
    # ), name='openapi-schema'),
     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]


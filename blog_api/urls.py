from django.urls import path
from .views import PostViewset
from rest_framework import routers

router=routers.DefaultRouter()

router.register('',PostViewset,basename='routes')

app_name='blog_api'


urlpatterns=router.urls
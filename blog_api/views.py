from rest_framework import generics
from rest_framework.decorators import APIView
from .serializers import PostSerializer,Post
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters



class PostViewset(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    serializer_class=PostSerializer
  
    queryset=Post.objects.all()
    def get_queryset(self):
        slug=self.request.query_params.get('slug',None)
        return Post.objects.filter(slug=slug)

    def get_object(self):
        item=self.kwargs.get('pk')
        return get_object_or_404(Post,slug=item)
    


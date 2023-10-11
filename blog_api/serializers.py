from rest_framework import serializers
from blog.models import Post
from rest_framework.validators import ValidationError
from rest_framework import reverse
from django.shortcuts import get_object_or_404

class PostSerializer(serializers.ModelSerializer):
    author_name=serializers.CharField(source='author.user_name',read_only=True)
    authors=serializers.SerializerMethodField(read_only=True)
    email=serializers.EmailField(source='author.email',read_only=True)
    slug=serializers.SerializerMethodField(read_only=True)
    url=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Post
        fields = ['id','title','authors','author','url','email','author_name','excerpt','content','slug','status']

    def get_authors(self,obj):
        return obj.author.user_name
    
    def get_slug(self,obj):
        return obj.slug
    
    def validate_title(self, value):
        # Access the incoming 'title' value in self.initial_data
        title = self.initial_data.get('title')

        # Perform your validation logic here
        if  not 'hello' in title :
            raise serializers.ValidationError({"title": "Title already exists."})

        return value
    
    def get_url(self,obj):
        request=self.context.get('request')
        if request is None:
            return None
        viewset_name = 'routes'
        action = 'detail'

        # Generate the URL using the reverse function
        url = reverse.reverse('token_verify', request=request)
        return url
from rest_framework import serializers
from django.contrib.auth.models import User
from BlogApi.models import Category, Post,Comment
        

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=('username','email')
        
class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True,many=True)
    class Meta:
        model = Comment
        fields=('__all__')

        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    author = UserSerializer(read_only=True,many=True)

    class Meta:
        model=  Post
        fields=('__all__')
        
        
class CategorySerializer(serializers.ModelSerializer):
    post=PostSerializer(read_only=True,many=True)

    class Meta:
        model = Category
        fields = ('__all__')

        
    
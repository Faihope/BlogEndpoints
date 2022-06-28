from imaplib import _Authenticator
from tokenize import Pointfloat
from rest_framework import serializers
from django.contrib.auth.models import User
from BlogApi.models import Category, Post,Comment
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','email','posts')
        
#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email' )
    extra_kwargs = {
      'email': {'required': True},
      'username': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
        


        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=('__all__')

        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    # user = UserSerializer(read_only=True,many=True)
    class Meta:
        model=  Post
        fields=('id','title','content','createdon','category','image','comments',)
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

        
    
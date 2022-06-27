
from email import message
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from BlogApi.api.serializers import CommentSerializer, PostSerializer,CategorySerializer, RegisterSerializer, UserSerializer
from BlogApi.models import Category,Post,Comment
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
# Create your views here.

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
  
@api_view(['GET','POST'])
def PostList(request):
    if request.method=='GET':
        posts= Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        posts=Post.objects.all()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET','PUT','DELETE'])       
def PostDetails(request,pk):
    if request.method=='GET':
        post = Post.objects.get(pk=pk)
        serializer= PostSerializer(post)
        return Response(serializer.data)
    if request.method=='PUT':
        post = Post.objects.get(pk=pk)
        serializer= PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method=='DELETE':
        post=Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST','GET'])       
def CategoryList(request):
    if request.method =='GET':
        categories=Category.objects.all() 
        serializer= CategorySerializer(categories,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        categories=Category.objects.all() 
        serializer= CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def categoryDetails(request,pk):
    if request.method =='GET':
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method=='DELETE':
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status =status.HTTP_201_CREATED)
    
@api_view(['POST','GET'])       
def CommentList(request):
    if request.method =='GET':
        comments=Comment.objects.all() 
        serializer= CommentSerializer(comments,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        comments=Comment.objects.all() 
        serializer= CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def commentDetails(request,pk):
    if request.method =='GET':
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    if request.method == 'PUT':
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method=='DELETE':
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status =status.HTTP_201_CREATED)
    
@api_view(['POST','GET'])       
def UserList(request):
    if request.method =='GET':
        users=User.objects.all() 
        serializer= UserSerializer(users,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        users=User.objects.all()
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def UserDetails(request,pk):
    if request.method =='GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method=='DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status =status.HTTP_201_CREATED)
    
        
        
        
        
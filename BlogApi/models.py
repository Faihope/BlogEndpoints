from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    image=models.ImageField(null=True,blank=False)
    content = models.CharField(max_length=2000)
    createdon = models.DateTimeField(auto_now_add=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    body=models.CharField(max_length=500)
    datecommented=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    
    def __str__(self):
        return self.post.title
    
  
    

    

    
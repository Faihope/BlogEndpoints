from BlogApi.api import views
from django.urls import path

urlpatterns = [
    path('',views.PostList,name='Home'),
    path('<int:pk>/',views.PostDetails,name='PostDetails'),
    path('category',views.CategoryList, name='categories'),
    path('category/<int:pk>',views.categoryDetails,name='categoryDetails'),
    path('comments',views.CommentList, name='comments'),
    path('comments/<int:pk>',views.commentDetails,name='comment'),              
    path('<int:pk>/comments',views.commentDetails,name='PostDetails'),
    # path('users',views.UserList,name='users'),
    # path('users/<int:pk>',views.UserDetails,name='UserDetails'),

]
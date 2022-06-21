from BlogApi.api import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('',views.PostList,name='Home'),
    path('<int:pk>/',views.PostDetails,name='PostDetails'),
    path('category',views.CategoryList, name='categories'),
    path('category/<int:pk>',views.categoryDetails,name='categoryDetails'),
    path('comments',views.CommentList, name='comments'),
    path('comments/<int:pk>',views.commentDetails,name='comment'),              
    path('<int:pk>/comments',views.commentDetails,name='PostDetails'),
    path('users',views.UserList,name='users'),
    path('users/<int:pk>',views.UserDetails,name='UserDetails'),
    path("get-details",views.UserDetailAPI.as_view()),
    path('register',views.RegisterUserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
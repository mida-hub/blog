from django.urls import path
from .views import CategoryListAPIView, TagListAPIView, PostListAPIView, PostDetailAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
]

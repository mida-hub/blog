from django.urls import path
from .views import CategoryListAPIView
from .views import TagListAPIView
from .views import PostListAPIView
from .views import TagFilteredPostListAPIView
from .views import PostDetailAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('posts/tags/<int:tags>/', TagFilteredPostListAPIView.as_view()),
]

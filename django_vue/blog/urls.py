from django.urls import path
from .views import CategoryListAPIView, TagListAPIView, PostListAPIView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),

]

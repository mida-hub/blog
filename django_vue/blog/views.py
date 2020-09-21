from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Category, Tag, Post
from .serializers import CategorySerializer, TagSerializer, PostSerializer


class TagListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PostListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

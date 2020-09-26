from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Category, Tag, Post, DummyAuth
from .serializers import CategorySerializer
from .serializers import TagSerializer
from .serializers import PostSerializer
from .serializers import PostDetailSerializer
from .serializers import DummyAuthSerializer


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
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class TagFilteredPostListAPIView(generics.ListAPIView):    
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    def get_queryset(self):
        tags = self.kwargs['tags']
        return Post.objects.filter(tags=tags)


class DummyAuthListAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = DummyAuthSerializer
    queryset = DummyAuth.objects.all()

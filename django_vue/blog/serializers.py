from rest_framework import serializers
from .models import Category, Tag, Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug',
            'timestamp'
        )
        read_only_fields = fields


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'timestamp'
        )
        read_only_fields = fields


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'category',
            'tags',
            'title',
            'content',
            'description',
            'created_at',
            'updated_at',
            'published_at',
            'is_public',
        )
        read_only_fields = fields

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
    formatted_published_at = serializers.SerializerMethodField('get_formatted_published_at')
    summarized_content = serializers.SerializerMethodField('get_summarized_content')
    # is_display = serializers.SerializerMethodField('get_is_display')

    def get_formatted_published_at(self, obj):
        import pendulum
        tz = pendulum.timezone('Asia/Tokyo')
        return tz.convert(obj.published_at).strftime('%Y-%m-%d %H:%M')

    def get_summarized_content(self, obj):
        cutLength = 80
        summarized_content = obj.content
        if len(summarized_content) > cutLength:
            summarized_content = summarized_content[:cutLength]
            summarized_content += '......'
        return summarized_content

    # def is_display(self, obj):
        # pass

    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'category',
            'tags',
            'title',
            'content',
            'summarized_content',
            'published_at',
            'formatted_published_at',
            'is_public'
        )
        read_only_fields = fields

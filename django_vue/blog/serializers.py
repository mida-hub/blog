from rest_framework import serializers
from .models import Category, Tag, Post
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

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
    is_display = serializers.SerializerMethodField('get_is_display')

    def get_formatted_published_at(self, obj):
        import pendulum
        tz = pendulum.timezone('Asia/Tokyo')
        return tz.convert(obj.published_at).strftime('%Y-%m-%d %H:%M')

    def get_text_markdownx(self, text):
        return mark_safe(markdownify(text))

    """
        コンテンツの最初の数行部分を概要して出す
        ToDo:一旦80文字にしているが特定のタグが最初に出てくる部分まで取るようにする
    """
    def get_summarized_content(self, obj):
        cut_length = 80
        summarized_content = obj.content
        if len(summarized_content) > cut_length:
            summarized_content = summarized_content[:cut_length]
            summarized_content += '......'
        return self.get_text_markdownx(summarized_content)

    """
        公開フラグ & 公開日付が現在日付より過去になった場合に表示する
    """
    def get_is_display(self, obj):
        import datetime

        published_at = (obj.published_at).strftime('%Y-%m-%d %H:%M')
        current_at = (datetime.datetime.now(datetime.timezone.utc)).strftime('%Y-%m-%d %H:%M')

        if obj.is_public and (published_at <= current_at):
            return True
        else:
            return False

    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'tags',
            'title',
            'summarized_content',
            'formatted_published_at',
            'is_public',
            'is_display'
        )
        read_only_fields = fields


class PostDetailSerializer(PostSerializer):
    decoded_content = serializers.SerializerMethodField('get_decoded_content')

    """
        Markdown コンテンツを HTML にデコード
    """
    def get_decoded_content(self, obj):
        return self.get_text_markdownx(obj.content)

    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'tags',
            'title',
            'decoded_content',
            'formatted_published_at',
            'is_public',
            'is_display'
        )
        read_only_fields = fields

from rest_framework import serializers
from .models import Category, Tag, Post, DummyAuth


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
    is_display = serializers.SerializerMethodField('get_is_display')
    with_prefix_title = serializers.SerializerMethodField('get_with_prefix_title')

    def get_formatted_published_at(self, obj):
        import pendulum
        tz = pendulum.timezone('Asia/Tokyo')
        return tz.convert(obj.published_at).strftime('%Y-%m-%d %H:%M')

    """
        公開日付が現在日付より過去かどうか判定する
    """
    def _published_at_is_past_day(self, obj):
        import datetime

        published_at = (obj.published_at).strftime('%Y-%m-%d %H:%M')
        current_at = (datetime.datetime.now(datetime.timezone.utc)).strftime('%Y-%m-%d %H:%M')

        return (published_at <= current_at)

    """
        公開フラグ & 公開日付が現在日付より過去になった場合に表示する
    """
    def get_is_display(self, obj):
        if obj.is_public and self._published_at_is_past_day(obj):
            return True
        else:
            return False

    """
        公開フラグ、公開日によってタイトルにプレフィックスを付与する
    """
    def get_with_prefix_title(self, obj):
        if obj.is_public and self._published_at_is_past_day(obj):
            return obj.title
        elif obj.is_public:
            return '[公開予約中]' +obj.title
        else:
            return '[編集中]' +obj.title


    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'tags',
            'with_prefix_title',
            'abstract',
            'formatted_published_at',
            'is_display'
        )
        read_only_fields = fields


class PostDetailSerializer(PostSerializer):
    abstract_content = serializers.SerializerMethodField('get_abstract_content')

    """
        概要とコンテンツを組み合わせて返す
    """
    def get_abstract_content(self, obj):
        return obj.abstract + '\n' + obj.content


    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'tags',
            'title',
            'abstract_content',
            'formatted_published_at',
            'is_display'
        )
        read_only_fields = fields


class DummyAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyAuth
        fields = (
            'id',
            'is_auth',
        )
        read_only_fields = fields

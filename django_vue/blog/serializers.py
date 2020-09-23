from rest_framework import serializers
from .models import Category, Tag, Post
import markdown

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
    with_prefix_title = serializers.SerializerMethodField('get_with_prefix_title')

    def get_formatted_published_at(self, obj):
        import pendulum
        tz = pendulum.timezone('Asia/Tokyo')
        return tz.convert(obj.published_at).strftime('%Y-%m-%d %H:%M')

    def _get_text_markdown(self, text):
        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc'])
        html = md.convert(text)
        return html

    """
        コンテンツの最初の数行部分を概要して出す
        最初に出てくる<h1>タグまでを取得する
        出てこなければ80文字分を返す
    """
    def get_summarized_content(self, obj):
        import re        
        decoded_content = self._get_text_markdown(obj.content)
        match_result = re.match('^(.*?)(<h1|<div)(.*?)>', decoded_content, re.S)

        if match_result is not None:
            # <h1>タグ & <div>タグ より前を取り出す
            return match_result[0].replace('<h1', '').replace('<div', '')
        else:
            cutLength = 80
            if len(decoded_content) > cutLength:
                decoded_content = decoded_content[:cutLength]
                decoded_content += '......'
                return decoded_content
            return decoded_content

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
            'summarized_content',
            'formatted_published_at',
            'is_display'
        )
        read_only_fields = fields


class PostDetailSerializer(PostSerializer):
    decoded_content = serializers.SerializerMethodField('get_decoded_content')

    """
        Markdown コンテンツを HTML にデコード
    """
    def get_decoded_content(self, obj):
        return self._get_text_markdown(obj.content)

    class Meta:
        model = Post
        depth = 1
        fields = (
            'id',
            'tags',
            'title',
            'content',
            'decoded_content',
            'formatted_published_at',
            'is_display'
        )
        read_only_fields = fields

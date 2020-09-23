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

    def get_formatted_published_at(self, obj):
        import pendulum
        tz = pendulum.timezone('Asia/Tokyo')
        return tz.convert(obj.published_at).strftime('%Y-%m-%d %H:%M')

    def get_text_markdown(self, text):
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
        decoded_content = self.get_text_markdown(obj.content)
        match_result = re.match('^(.*?)(<h1|<div)(.*?)>', decoded_content, re.S)

        if match_result:
            # <h1>タグ & <div>タグ より前を取り出す
            return match_result[0].split('<h1')[0].split('<div')[0]
        else:
            cutLength = 80
            if len(decoded_content) > cutLength:
                decoded_content = decoded_content[:cutLength]
                decoded_content += '......'
                return decoded_content
            return decoded_content

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
        return self.get_text_markdown(obj.content)

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

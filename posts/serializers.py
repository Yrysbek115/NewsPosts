from rest_framework import serializers
from .models import Post


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link', 'author_name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'upvote_amount', 'created_at', 'updated_at')


class PostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'upvote_amount', 'created_at', 'updated_at')

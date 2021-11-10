from rest_framework import serializers
from .models import Post, Comment


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link', 'author_name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'upvote_amount', 'created_at', 'updated_at')


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ('post', 'content', 'author_name')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id',  'content', 'author_name', 'created_at', 'updated_at')


class PostDetailsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'upvote_amount', 'created_at', 'updated_at', 'comments')


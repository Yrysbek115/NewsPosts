from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import PostSerializer, PostCreateUpdateSerializer, PostDetailsSerializer, CommentSerializer, \
    CommentCreateUpdateSerializer
from posts.services import PostServices, CommentServices


class PostListCreateView(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return PostServices.get_queryset()

    def post(self, request, *args, **kwargs):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={
                'message': "Invalid input",
                'errors': serializer.errors
            },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        new = PostServices.create(**serializer.validated_data)
        data = PostSerializer(instance=new).data
        return Response(data=data, status=status.HTTP_201_CREATED)


class PostDetailsView(APIView):

    def get(self, request, pk):
        post = PostServices.get(pk=pk)
        data = PostDetailsSerializer(post).data
        return Response(data=data)

    def put(self, request, pk):
        serializer = PostCreateUpdateSerializer(data=request.data)
        post = PostServices.get(pk=pk)
        if not serializer.is_valid():
            return Response(data={
                'message': "Invalid input",
                'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        updated_post = PostServices.update(post=post,
            **serializer.validated_data)
        data = PostSerializer(updated_post).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        post = PostServices.get(pk=pk)
        PostServices.delete(post=post)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostUpvoteView(APIView):
    def post(self, request, pk):
        post = PostServices.get(pk=pk)
        PostServices.upvote(post=post)
        data = PostDetailsSerializer(post).data
        return Response(data=data)


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = CommentCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={
                'message': "Invalid input",
                'errors': serializer.errors
            },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        new = CommentServices.create(**serializer.validated_data)
        data = CommentSerializer(instance=new).data
        return Response(data=data, status=status.HTTP_201_CREATED)


class CommentDetailsView(APIView):
    def get(self, request, pk):
        comment = CommentServices.get(pk=pk)
        data = CommentSerializer(comment).data
        return Response(data=data)

    def put(self, request, pk):
        serializer = CommentCreateUpdateSerializer(data=request.data)
        post_comment = CommentServices.get(pk=pk)
        if not serializer.is_valid():
            return Response(data={
                'message': "Invalid input",
                'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        comment = CommentServices.update(comment=post_comment, **serializer.validated_data)
        data = CommentSerializer(comment).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        comment = CommentServices.get(pk=pk)
        CommentServices.delete(comment=comment)
        return Response(status=status.HTTP_204_NO_CONTENT)

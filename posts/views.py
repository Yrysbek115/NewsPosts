from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import PostSerializer, PostCreateUpdateSerializer, PostDetailsSerializer
from posts.services import PostServices


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
        e_learning = PostServices.get(pk=pk)
        data = PostDetailsSerializer(e_learning).data
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
        updated_e_learning = PostServices.update(post=post,
            **serializer.validated_data)
        data = PostSerializer(updated_e_learning).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        post = PostServices.get(pk=pk)
        PostServices.delete(post=post)
        return Response(status=status.HTTP_204_NO_CONTENT)


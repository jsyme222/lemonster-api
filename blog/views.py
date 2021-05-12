from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class BlogPostView(APIView):
    def get(self, request, *args, **kwargs):
        id = request.GET["id"] if "id" in request.GET.keys() else None
        if id:
            try:
                post = BlogPost.objects.get(id=id)
                serialized_post = BlogPostSerializer(post)
                return Response(serialized_post.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist as e:
                return Response({"error": f'no post {id}'}, status=status.HTTP_204_NO_CONTENT)
        all_posts = BlogPost.objects.all()
        serialized_posts = BlogPostSerializer(all_posts, many=True)
        print(serialized_posts.data)
        return Response(serialized_posts.data, status=status.HTTP_200_OK)

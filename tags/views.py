from rest_framework.views import APIView
from tags.models import BlogTag
from tags.models import BlogTag
from tags.serializers import BlogTagSerializer
from rest_framework import status
from rest_framework.response import Response



class BlogTagView(APIView):
    def get(self, request, *args, **kwargs):
        tags = BlogTag.objects.order_by("title")
        if "all" not in request.GET.keys():
            tags = tags.filter(usage_count__gt=0)
        serialized_tags = BlogTagSerializer(tags, many=True)
        return Response(serialized_tags.data, status=status.HTTP_200_OK)
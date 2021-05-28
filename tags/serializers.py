from rest_framework.serializers import ModelSerializer
from tags.models import BlogTag


class BlogTagSerializer(ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ("title", "id")
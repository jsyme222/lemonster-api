from projects.serializers import ChipTagSerializer
from rest_framework.serializers import ModelSerializer, Serializer
from blog.models import BlogPost


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"

    tags = ChipTagSerializer(many=True)

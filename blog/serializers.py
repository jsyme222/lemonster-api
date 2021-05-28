from tags.serializers import BlogTagSerializer
from rest_framework.serializers import ModelSerializer
from blog.models import BlogPost


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"

    tags = BlogTagSerializer(many=True)

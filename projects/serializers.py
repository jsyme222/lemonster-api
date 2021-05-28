from rest_framework.serializers import ModelSerializer

from projects.models import Project
from tags.serializers import BlogTagSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    core_deps = BlogTagSerializer(many=True)


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "slug", "title", "created_on", "description", "content",
                  "core_deps", "backgroundImage", "backgroundImageUpload", "url", "repo", "rating")

    core_deps = BlogTagSerializer(many=True)

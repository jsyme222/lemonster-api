from django.db.models import fields
from rest_framework import serializers

from projects.models import ClientContentDocument, ClientContentWritten, ClientSuppliedContent, Project
from tags.serializers import BlogTagSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    core_deps = BlogTagSerializer(many=True)


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "slug", "title", "created_on", "description", "content",
                  "core_deps", "backgroundImage", "backgroundImageUpload", "url", "repo", "rating")

    core_deps = BlogTagSerializer(many=True)


class ClientDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContentDocument
        fields = "__all__"


class ClientContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContentWritten
        fields = "__all__"


class ClientSuppliedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSuppliedContent
        fields = "__all__"

    def get_project(self, inst):
        return inst.project.title

    project = serializers.SerializerMethodField()
    content_written = ClientContentSerializer(many=True)
    content_documents = ClientDocumentSerializer(many=True)

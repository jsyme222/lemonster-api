from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from projects.models import ChipTag, Project


class ChipTagSerializer(ModelSerializer):
    class Meta:
        model = ChipTag
        fields = [
            "title"
        ]


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    core_deps = ChipTagSerializer(many=True)

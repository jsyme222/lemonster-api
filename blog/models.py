from projects.models import ChipTag
from django.db import models
from django.utils import timezone
import uuid


class BlogPost(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True)
    title = models.CharField(
        max_length=250,
        blank=False,
        default=""
    )
    created_on = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )
    background = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    content = models.TextField(
        blank=True,
        default="",
        null=True
    )
    tags = models.ManyToManyField(
        ChipTag,
        related_name="blog_tags"
    )

    def __str__(self) -> str:
        return self.title

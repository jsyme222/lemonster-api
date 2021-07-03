from blog.signals import set_blog_tag_usage
from tags.models import BlogTag
from django.db import models
from django.utils import timezone
from django.db.models.signals import m2m_changed
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
        null=True,
        help_text="http://..."
    )
    content = models.TextField(
        blank=True,
        default="",
        null=True
    )
    tags = models.ManyToManyField(
        BlogTag,
        related_name="blog_tags",
        blank=True
    )

    def __str__(self) -> str:
        return self.title


m2m_changed.connect(set_blog_tag_usage, sender=BlogPost.tags.through,
                    dispatch_uid="blogpost.tags.change")

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class ChipTag(models.Model):
    title = models.CharField(
        max_length=250,
        blank=False,
        default=""
    )

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    title = models.CharField(
        max_length=250,
        blank=False,
        default=""
    )
    slug = models.SlugField(blank=True, null=True, default="")
    created_on = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )
    url = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    backgroundImage = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    description = models.TextField(
        blank=True,
        default="",
        null=True
    )
    repo = models.CharField(
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
    core_deps = models.ManyToManyField(
        ChipTag,
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        self.slug = slug
        return super(Project, self).save(*args, **kwargs)

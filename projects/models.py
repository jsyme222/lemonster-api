from api.utils.filecleanup import image_file_cleanup
from tags.models import Tag
from documents.models import Document
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_delete
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Project(models.Model):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    RATING_CHOICES = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )

    title = models.CharField(
        max_length=250,
        blank=False,
        default=""
    )
    slug = models.SlugField(blank=True, null=True, default="")
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)
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
    backgroundImageUpload = models.ImageField(
        upload_to='projects', null=True, blank=True)
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
    content = MarkdownField(rendered_field='content_rendered',
                            validator=VALIDATOR_STANDARD, null=True, blank=True)

    content_rendered = RenderedMarkdownField(null=True)
    core_deps = models.ManyToManyField(
        Tag,
        blank=True
    )

    #  Data left out of standard API calls
    documents = models.ManyToManyField(Document, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        self.slug = slug
        return super(Project, self).save(*args, **kwargs)


class ClientContentWritten(models.Model):
    question = models.CharField(max_length=1200, default="")
    answer = models.TextField(default="")


class ClientSuppliedContent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    written_content = models.ManyToManyField(ClientContentWritten)


post_delete.connect(image_file_cleanup, sender=Project,
                    dispatch_uid="projects.image.file_cleanup")

from api.utils.filecleanup import image_file_cleanup
from tags.models import Tag
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_delete


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
    content = models.TextField(
        blank=True,
        default="",
        null=True
    )
    core_deps = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        self.slug = slug
        return super(Project, self).save(*args, **kwargs)


post_delete.connect(image_file_cleanup, sender=Project,
                    dispatch_uid="projects.image.file_cleanup")

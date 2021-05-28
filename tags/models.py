from django.db import models


class AbstractTag(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=250,
        blank=False,
        default=""
    )

    def __str__(self) -> str:
        return self.title


class Tag(AbstractTag):
    pass


class BlogTag(Tag):
    pass

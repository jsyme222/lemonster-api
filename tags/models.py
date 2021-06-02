from django.db import models
from django.db.models.fields import IntegerField


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
    class Meta:
        app_label = "blog"

    usage_count = models.PositiveIntegerField(default=0)

    def set_usage(self, value: bool = False) -> int:
        value = 1 if value else -1 if self.usage_count >= 1 else 0
        print("VALUE TO TAG: ", value)
        self.usage_count += value
        print(self.usage_count)
        self.save()
        return self.usage_count

    @property
    def is_active(self):
        return self.usage_count >= 1

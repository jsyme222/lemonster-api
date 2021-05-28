from django.db import models
from django.utils import timezone


class DocumentType(models.Model):
    title = models.CharField(max_length=250, default="")
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title or self.id


class AbstractDocument(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=250, default="")
    file = models.FileField(upload_to="documents/")
    created_on = models.DateTimeField(default=timezone.now)
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title or str(self.id)


class Document(AbstractDocument):
    pass


class PrivateDocument(AbstractDocument):
    file = models.FileField(upload_to="documents/.private/")

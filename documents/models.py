from api.utils.filecleanup import encrypted_file_cleanup, file_cleanup
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django_cryptography.fields import encrypt
from django_encrypted_filefield.fields import EncryptedFileField


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
    doc_type = models.ForeignKey(
        DocumentType, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(default="", blank=True, null=True)

    def __str__(self) -> str:
        return self.title or str(self.id)


class Document(AbstractDocument):
    pass


class PrivateDocument(AbstractDocument):
    file = EncryptedFileField(upload_to="documents/private/")
    notes = encrypt(models.TextField(default="", blank=True, null=True))


post_delete.connect(file_cleanup, sender=Document,
                    dispatch_uid="documents.document.file_cleanup")

post_delete.connect(encrypted_file_cleanup, sender=PrivateDocument,
                    dispatch_uid="documents.private_document.file_cleanup")

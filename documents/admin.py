from django.contrib import admin
from documents.models import DocumentType, Document, PrivateDocument


@admin.register(DocumentType, Document, PrivateDocument)
class DocumentAdmin(admin.ModelAdmin):
    pass

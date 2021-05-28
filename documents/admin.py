from django.contrib import admin
from documents.models import Document, PrivateDocument


@admin.register(Document, PrivateDocument)
class DocumentAdmin(admin.ModelAdmin):
    pass

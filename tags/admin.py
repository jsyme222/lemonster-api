from tags.models import BlogTag, Tag
from django.contrib import admin


@admin.register(Tag, BlogTag)
class TagAdmin(admin.ModelAdmin):
    pass

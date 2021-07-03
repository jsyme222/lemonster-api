from blog.models import BlogPost
from django.contrib import admin


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = (
        ("General", {
            "fields": ("id", "created_on")
        }),
        ("Image", {
            "fields": ("background", )
        }),
        ("Content", {
            "fields": ("title", "tags", "content")
        })
    )

from blog.models import BlogPost
from django.contrib import admin


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

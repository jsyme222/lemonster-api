from projects.models import Project
from django.contrib import admin


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

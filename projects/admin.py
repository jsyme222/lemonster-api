from projects.models import ChipTag, Project
from django.contrib import admin


@admin.register(ChipTag, Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

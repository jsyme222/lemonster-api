from projects.models import Project, ClientSuppliedContent, ClientContentWritten
from django.contrib import admin


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientContentWritten, ClientSuppliedContent)
class ClientContentAdmin(admin.ModelAdmin):
    pass

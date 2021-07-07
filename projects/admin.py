from projects.models import ClientContentDocument, Project, ClientSuppliedContent, ClientContentWritten
from django.contrib import admin


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientContentWritten, ClientSuppliedContent, ClientContentDocument)
class ClientContentAdmin(admin.ModelAdmin):
    pass

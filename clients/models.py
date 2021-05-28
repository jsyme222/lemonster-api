from documents.models import Document
from projects.models import Project
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250, default="")

    def __str__(self) -> str:
        return self.name
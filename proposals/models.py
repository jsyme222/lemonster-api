from clients.models import Client
from tags.models import Tag
from django.db import models


class ProposalTheme(models.Model):
    title = models.CharField(max_length=250, default="")

    def __str__(self) -> str:
        return self.title or self.id


class Proposal(models.Model):
    client = models.ForeignKey(Client, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default="")
    objective = models.TextField(default="", blank=True)
    timeline = models.PositiveIntegerField(default=0, blank=True)
    work_type = models.ManyToManyField(Tag, blank=True)

    theme = models.ForeignKey(ProposalTheme, null=True,
                              on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title or self.id

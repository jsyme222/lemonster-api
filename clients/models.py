from documents.models import Document
from projects.models import Project
from django.db import models


class Client(models.Model):
    display_name = models.CharField(max_length=250, default="")
    name_first = models.CharField(max_length=250, default="")
    name_last = models.CharField(max_length=250, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=12, default="")
    company = models.CharField(max_length=250, default="")
    billing_address = models.CharField(max_length=250, default="")
    shipping_address = models.CharField(max_length=250, default="")
    website = models.URLField(max_length=250, default="")
    

    def __str__(self) -> str:
        return self.name
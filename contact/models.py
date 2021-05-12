from django.db import models
from django.utils import timezone


class ContactMail(models.Model):
    name = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    created_on = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )
    email = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    phone = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    company = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True
    )
    website = models.CharField(
        max_length=250,
        blank=True,
        default="",
        null=True,
    )
    questions = models.TextField(
        blank=True,
        default="",
        null=True
    )
    services_website = models.BooleanField(
        default=False, verbose_name="Website Services")
    services_business_application = models.BooleanField(
        default=False, verbose_name="Application Services")
    services_maintenance = models.BooleanField(
        default=False, verbose_name="Maintenance")
    services_other = models.BooleanField(
        default=False, verbose_name="Other Services")

    def __str__(self) -> str:
        return f'{self.name} on {self.created_on}'

from contact.models import ContactMail
from django.contrib import admin


@admin.register(ContactMail)
class ContactAdmin(admin.ModelAdmin):
    pass

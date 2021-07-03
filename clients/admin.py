from clients.models import Client
from django.contrib import admin


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Name", {
            "fields": ("display_name", "name_first", "name_last")
        }),
        ("Contact", {
            "fields": ("email", "phone", "billing_address", "shipping_address")
        }),
        ("Details", {
            "fields": ("company", "website")
        })
    )

from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from contact.models import ContactMail


class ContactMailSerializer(ModelSerializer):
    class Meta:
        model = ContactMail
        fields = "__all__"

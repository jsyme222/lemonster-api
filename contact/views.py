from contact.serializers import ContactMailSerializer
from contact.models import ContactMail
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ContactMailView(APIView):
    def post(self, request, *args, **kwargs):
        mail = request.data
        new_mail = {
            "name": mail["name"],
            "email": mail["email"],
            "phone": mail["phone"],
            "company": mail["company"],
            "website": mail["website"],
            "questions": mail["questions"],
            "services_website": mail["services"]["website"],
            "services_business_application": mail["services"]["businessApplication"],
            "services_maintenance": mail["services"]["maintenance"],
            "services_other": mail["services"]["other"],
        }
        mailObj = ContactMail.objects.create(**new_mail)
        serialized_mail = ContactMailSerializer(mailObj)
        return Response(serialized_mail.data, status=status.HTTP_200_OK)

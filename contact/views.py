from typing import Mapping
from contact.serializers import ContactMailSerializer
from contact.models import ContactMail
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from api.settings import SMTP_PASS, SMTP_EMAIL, BG_COLORS


def check_key(obj, key, callback_value=""):
    try:
        if key in obj.keys():
            return obj[key]
    except KeyError as e:
        return callback_value


class ContactMailView(APIView):
    def send_mail(self, message) -> bool:
        port = 465  # For SSL
        password = SMTP_PASS
        to_address = SMTP_EMAIL
        from_address = message["email"]

        html_message = MIMEMultipart("alternative")

        html_message["Subject"] = "Lemonster.dev Contact Form"
        html_message["From"] = "LeMonster.dev"
        html_message["To"] = to_address
        # Create the plain-text and HTML version of your message

        text = f'You have a message from Lemonster.dev: {message}'
        html = (
            '<html>'
            '<body style="background-color: #356e40">'
            '<div style="max-width:350px; padding:2rem; background: #232323; color: whitesmoke;margin:0 auto;">'
            f'<p>NAME: {check_key(message, "name")}</p>'
            f'<p>EMAIL: {check_key(message, "email")}</p>'
            f'<p>PHONE: <a href="tel:{check_key(message, "phone")}">{check_key(message, "phone")}</a></p>'
            f'<p>COMPANY: {check_key(message, "company")}</p>'
            f'<p>WEBSITE: {check_key(message, "website")}</p>'
            f'<p>QUESTIONS: {check_key(message, "questions")}</p>'
            '<p><b>SERVICES REQUESTED</b></p>'
            f'<p>WEBSITE: <span style="">{check_key(message, "services_website")}</span></p>'
            f'<p>APPLICATION: <span style="">{check_key(message, "services_business_application")}</span></p>'
            f'<p>MAINTENANCE: <span style="">{check_key(message, "services_maintenance")}</span></p>'
            f'<p>OTHER: <span style="">{check_key(message, "services_other")}</span></p>'
            '</div>'
            '</body>'
            '</html>'
        )

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        html_message.attach(part1)
        html_message.attach(part2)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

            try:
                server.login(to_address, password)
                server.sendmail(
                    from_address, to_address, html_message.as_string()
                )
                print(BG_COLORS["OKGREEN"], f'mail sent to {to_address}')
            except Exception as e:
                print(BG_COLORS["FAIL"],
                      "ERROR: smpt unable to login to server.")
                return False
            return True

    def post(self, request, *args, **kwargs):
        def init_kwargs(model, arg_dict):
            model_fields = [f.name for f in model._meta.get_fields()]
            return {k: v for k, v in arg_dict.items() if k in model_fields}

        mail = request.data
        new_mail = {x: check_key(mail, x) for x in mail.keys()}
        print(mail)
        if "email" in new_mail.keys():
            new_mail = init_kwargs(ContactMail, new_mail)
            mailObj = ContactMail.objects.create(**new_mail)
            serialized_mail = ContactMailSerializer(mailObj)
            mail_sent = self.send_mail(serialized_mail.data)
            if not mail_sent:
                return Response(
                    {"error": "smtp"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response({"error": "no email provided"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serialized_mail.data, status=status.HTTP_200_OK)

"""documents URL Configuration
"""
from django.urls import re_path
from django_encrypted_filefield.constants import FETCH_URL_NAME
from documents.views import FetchView


urlpatterns = [
    re_path(r"^fetch(?P<path>.+)", FetchView.as_view(), name=FETCH_URL_NAME)
]

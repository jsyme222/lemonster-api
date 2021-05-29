"""projects URL Configuration
"""
from tags.views import BlogTagView
from django.urls import path

urlpatterns = [
    path("blog", BlogTagView.as_view()),
]

"""projects URL Configuration
"""
from projects.views import ChipTagView, ProjectView
from django.urls import path

urlpatterns = [
    path("", ProjectView.as_view()),
    path("tags/", ChipTagView.as_view()),
]

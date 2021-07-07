"""projects URL Configuration
"""
from projects.views import ClientContentView, ProjectView
from django.urls import path

urlpatterns = [
    path("", ProjectView.as_view()),
    path("client-content", ClientContentView.as_view())
]

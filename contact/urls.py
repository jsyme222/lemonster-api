"""blog URL Configuration
"""
from contact.views import ContactMailView
from blog.views import BlogPostView
from django.urls import path

urlpatterns = [
    path("", BlogPostView.as_view()),
    path("mail/", ContactMailView.as_view())
]

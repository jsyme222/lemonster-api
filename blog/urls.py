"""blog URL Configuration
"""
from blog.views import BlogPostView
from django.urls import path

urlpatterns = [
    path("", BlogPostView.as_view(), name="post_view"),
]

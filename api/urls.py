"""api URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from api.settings import DEBUG, MEDIA_ROOT, MEDIA_URL, VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path(f'v{VERSION}/projects/', include('projects.urls')),
    path(f'v{VERSION}/blog/', include('blog.urls')),
    path(f'v{VERSION}/contact/', include('contact.urls')),
    path(f'v{VERSION}/documents/', include('documents.urls')),
    path(f'v{VERSION}/tags/', include('tags.urls')),
    path(f'v{VERSION}/proposals/', include('proposals.urls')),
    path(f'v{VERSION}/gql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
if DEBUG:
    urlpatterns += static(MEDIA_URL,
                          document_root=MEDIA_ROOT)

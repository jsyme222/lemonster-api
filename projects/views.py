from rest_framework import response
from projects.serializers import ClientSuppliedContentSerializer, ProjectListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import ClientSuppliedContent, Project
from django.core.exceptions import ObjectDoesNotExist


class ProjectView(APIView):

    def get_project(self, slug):
        try:
            project = Project.objects.get(slug=slug)
            return project
        except ObjectDoesNotExist as e:
            return False

    def get(self, request, *args, **kwargs):
        slug = request.GET["slug"] if "slug" in request.GET.keys() else None
        if slug:
            if project := self.get_project(slug):
                project = ProjectListSerializer(project)
                return Response(project.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": f'no project {slug}'}, status=status.HTTP_200_OK)
        all_projects = Project.objects.all().order_by("-rating")
        serialized_projects = ProjectListSerializer(all_projects, many=True)
        return Response(serialized_projects.data, status=status.HTTP_200_OK)


class ClientContentView(APIView):

    def get(self, request, *args, **kwargs):
        client_content = {}
        params = request.GET.keys()
        if "c" in params:
            content_id = request.GET["c"]
            try:
                content = ClientSuppliedContent.objects.get(id=content_id)
                client_content = ClientSuppliedContentSerializer(content)
                print(client_content.data)
            except ClientSuppliedContent.DoesNotExist:
                client_content = {"ERROR": "No Content"}
        return Response(client_content.data, status=status.HTTP_200_OK)

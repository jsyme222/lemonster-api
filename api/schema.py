import graphene
from graphene_django import DjangoObjectType

from projects.models import ChipTag, Project
from blog.models import BlogPost


class TagType(DjangoObjectType):
    class Meta:
        model = ChipTag
        fields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost
        fields = "__all__"


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    project_by_title = graphene.Field(
        ProjectType, title=graphene.String(required=True))
    project_search = graphene.List(
        ProjectType, title=graphene.String(required=True))
    all_posts = graphene.List(BlogPostType)
    post_by_title = graphene.Field(
        BlogPostType, title=graphene.String(required=True))

    def resolve_all_posts(self, info):
        return BlogPost.objects.all()

    def resolve_post_by_title(root, info, title):
        try:
            return BlogPost.objects.get(title=title)
        except BlogPost.DoesNotExist:
            return None

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_project_by_title(root, info, title):
        try:
            return Project.objects.get(title=title)
        except Project.DoesNotExist:
            return None

    def resolve_project_search(root, info, title):
        try:
            projs = Project.objects.filter(title__icontains=title)
            if projs[0]:
                return projs
        except IndexError:
            return None


schema = graphene.Schema(query=Query)

from rest_framework.viewsets import ModelViewSet

from apis.translation.models import Project
from apis.translation.serializers import ProjectSerializer
from apis.translation.filters import ProjectFilter


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

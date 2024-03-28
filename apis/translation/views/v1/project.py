from rest_framework.viewsets import ModelViewSet

from apis.translation.models import Project
from apis.translation.serializers import ProjectSerializer, ProjectForListSerializer, ProjectForCreateSerializer
from apis.translation.filters import ProjectFilter


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectForListSerializer
        elif self.action == 'create':
            return ProjectForCreateSerializer
        return super().get_serializer_class()

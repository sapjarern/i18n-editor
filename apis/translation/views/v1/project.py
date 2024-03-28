from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from apis.translation.models import Project, Translate
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
    
    @action(methods=["GET"], detail=True)
    def export(self, request, pk, *args, **kwargs):
        project = self.get_object()
        context = {}
        print(f'{len(Translate.objects.filter(language__in=project.language.all(), translation_key__project=project)) = }')
        for translate in Translate.objects.filter(language__in=project.language.all(), translation_key__project=project):
            if translate.language.code not in context:
                context.update({translate.language.code: {translate.translation_key.key: translate.translate}})
            else:
                context[translate.language.code].update({translate.translation_key.key: translate.translate})
        return Response(context, status=status.HTTP_200_OK)

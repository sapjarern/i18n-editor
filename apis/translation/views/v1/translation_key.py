from rest_framework.viewsets import ModelViewSet

from apis.translation.models import TranslationKey
from apis.translation.serializers import TranslationKeySerializer, TranslationKeyForListSerializer, \
    TranslationKeyForCreateSerializer, TranslationKeyForDetailSerializer, TranslationKeyForUpdateSerializer
from apis.translation.filters import TranslationKeyFilter


class TranslationKeyViewset(ModelViewSet):
    queryset = TranslationKey.objects.all()
    serializer_class = TranslationKeySerializer
    filterset_class = TranslationKeyFilter

    def get_queryset(self):
        return self.queryset.filter(project=self.request.project)

    def get_serializer_class(self):
        if self.action == 'list':
            return TranslationKeyForListSerializer
        elif self.action == 'create':
            return TranslationKeyForCreateSerializer
        elif self.action == 'retrieve':
            return TranslationKeyForDetailSerializer
        elif self.action in ['update', 'partial_update']:
            return TranslationKeyForUpdateSerializer
        return super().get_serializer_class()

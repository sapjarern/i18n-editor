from rest_framework.viewsets import ModelViewSet

from apis.translation.models import Translate
from apis.translation.serializers import TranslateSerializer, TranslateForListSerializer, TranslateForCreateSerializer
from apis.translation.filters import TranslateFilter


class TranslateViewset(ModelViewSet):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer
    filterset_class = TranslateFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TranslateForListSerializer
        elif self.action == 'create':
            return TranslateForCreateSerializer
        return super().get_serializer_class()

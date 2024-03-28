from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from apis.translation.models import Translate
from apis.translation.serializers import TranslateSerializer, TranslateForListSerializer, TranslateForCreateSerializer
from apis.translation.filters import TranslateFilter


class TranslateViewset(ListModelMixin, GenericViewSet):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer
    filterset_class = TranslateFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TranslateForListSerializer
        return super().get_serializer_class()

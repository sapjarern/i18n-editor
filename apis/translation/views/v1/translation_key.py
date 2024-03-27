from rest_framework.viewsets import ModelViewSet

from apis.translation.models import TranslationKey
from apis.translation.serializers import TranslationKeySerializer
from apis.translation.filters import TranslationKeyFilter


class TranslationKeyViewset(ModelViewSet):
    queryset = TranslationKey.objects.all()
    serializer_class = TranslationKeySerializer
    filterset_class = TranslationKeyFilter

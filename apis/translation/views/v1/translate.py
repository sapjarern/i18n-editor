from rest_framework.viewsets import ModelViewSet

from apis.translation.models import Translate
from apis.translation.serializers import TranslateSerializer
from apis.translation.filters import TranslateFilter


class TranslateViewset(ModelViewSet):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer
    filterset_class = TranslateFilter

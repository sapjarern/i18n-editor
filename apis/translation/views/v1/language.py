from rest_framework.viewsets import ModelViewSet

from apis.translation.models import Language
from apis.translation.serializers import LanguageSerializer
from apis.translation.filters import LanguageFilter


class LanguageViewset(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filterset_class = LanguageFilter

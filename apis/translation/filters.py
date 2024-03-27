from django_filters import filters, FilterSet

from apis.translation.models import Language, Project, TranslationKey, Translate


class LanguageFilter(FilterSet):
    code = filters.CharFilter(field_name='code', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Language
        fields = ['code', 'title']


class ProjectFilter(FilterSet):
    code = filters.CharFilter(field_name='code', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['code', 'title']


class TranslationKeyFilter(FilterSet):
    key = filters.CharFilter(field_name='key', lookup_expr='icontains')

    class Meta:
        model = TranslationKey
        fields = ['key']


class TranslateFilter(FilterSet):
    translation_key = filters.ModelMultipleChoiceFilter(queryset=TranslationKey.objects.all())
    language = filters.ModelMultipleChoiceFilter(queryset=Language.objects.all())

    class Meta:
        model = Translate
        fields = ['translation_key', 'language']

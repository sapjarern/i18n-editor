from rest_framework import serializers

from apis.translation.models import Language, Project, TranslationKey, Translate


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['code', 'title']


class ProjectSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True)

    class Meta:
        model = Project
        fields = ['code', 'title', 'description', 'language']


class ProjectForListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True)

    class Meta:
        model = Project
        fields = ['code', 'title', 'description', 'language']


class ProjectForCreateSerializer(serializers.ModelSerializer):
    language = serializers.ManyRelatedField(child_relation=serializers.CharField())
    description = serializers.CharField(required=False)

    class Meta:
        model = Project
        fields = ['code', 'title', 'description', 'language']


class ProjectMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['code', 'title']


class TranslationKeySerializer(serializers.ModelSerializer):
    project = ProjectMinimalSerializer()

    class Meta:
        model = TranslationKey
        fields = ['key', 'project']


class TranslationKeyForListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslationKey
        fields = ['id', 'key']


class TranslationKeyForCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source='pk')
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True)

    def to_internal_value(self, data):
        if request := self.context.get('request', None):
            if request.project:
                data.update({'project': request.project.pk})
        data = super().to_internal_value(data)
        
        return data
    
    class Meta:
        model = TranslationKey
        fields = ['id', 'key', 'project']


class TranslationKeyForDetailSerializer(serializers.ModelSerializer):
    translate = serializers.SerializerMethodField()

    @staticmethod
    def get_translate(instance):
        return dict((key, val) for key, val in instance.translation_key_translate.all().values_list('language__code', 'translate'))

    class Meta:
        model = TranslationKey
        fields = ['key', 'translate']


class TranslateSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = Translate
        fields = ['translate', 'language', 'translation_key']


class TranslateForListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    translation_key = serializers.CharField()

    class Meta:
        model = Translate
        fields = ['id', 'translate', 'language', 'translation_key']


class TranslateForCreateSerializer(serializers.ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    translation_key = serializers.CharField()

    def to_internal_value(self, data):
        print(f'{data = }')
        if translation_key := data.get('translation_key'):
            TranslationKey.objects.filter(key=translation_key).first()
        return super().to_internal_value(data)

    class Meta:
        model = Translate
        fields = ['translate', 'language', 'translation_key']


class TranslationKeyForUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslationKey
        fields = ['key']

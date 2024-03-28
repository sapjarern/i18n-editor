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
        fields = ['id', 'code', 'title', 'description', 'language']


class ProjectForListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'code', 'title', 'description', 'language']


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


class TranslateForTranslationKeyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translate
        fields = ['translate', 'language']


class TranslateForTranslationKeyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translate
        fields = ['translate', 'language']


class TranslationKeyForDetailSerializer(serializers.ModelSerializer):
    translates = serializers.SerializerMethodField()

    @staticmethod
    def get_translates(instance):
        return TranslateForTranslationKeyDetailSerializer(instance.translation_key_translate.all(), many=True).data

    class Meta:
        model = TranslationKey
        fields = ['key', 'translates']


class TranslateForCreateSerializer(serializers.Serializer):
    translate = serializers.CharField()
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    translation_key = serializers.PrimaryKeyRelatedField(queryset=TranslationKey.objects.all())

    def to_internal_value(self, data):
        print(f'{data = }')
        if 'translation_key' not in data:
            translation_key = self.context.get('translation_key')
            if isinstance(translation_key, TranslationKey):
                translation_key = translation_key.pk
            data.update({'translation_key': translation_key})
        return super().to_internal_value(data)

    class Meta:
        model = Translate
        fields = ['translate', 'language', 'translation_key']


class TranslationKeyForUpdateSerializer(serializers.ModelSerializer):
    translates = TranslateForCreateSerializer(many=True, write_only=True)

    def to_internal_value(self, data):
        self.context.update({'translation_key': self.instance})
        return super().to_internal_value(data)

    def update(self, instance, validated_data):
        translates = validated_data.pop('translates', [])
        print(f'{translates = }')
        for translate in translates:
            value = translate.pop('translate', '')
            try:
                Translate.objects.update_or_create(**translate, defaults={'translate': value})
            except Exception as e:
                print(f'{e = }')
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['translates'] = TranslateForTranslationKeyDetailSerializer(instance.translation_key_translate.all(), many=True).data
        return data

    class Meta:
        model = TranslationKey
        fields = ['key', 'translates']

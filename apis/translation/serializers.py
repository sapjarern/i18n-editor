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


class ProjectMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['code', 'title']


class TranslationKeySerializer(serializers.ModelSerializer):
    project = ProjectMinimalSerializer()

    class Meta:
        model = TranslationKey
        fields = ['key', 'project']


class TranslateSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    translation_key = ProjectMinimalSerializer()

    class Meta:
        model = Translate
        fields = ['translate', 'language', 'translation_key']

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE,
    #                                related_name='created_by_%(class)s')
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE,
    #                                related_name='updated_by_%(class)s')

    class Meta:
        abstract = True

class Language(BaseModel):

    code = models.CharField(primary_key=True, blank=False, null=False, max_length=10)
    title = models.CharField(blank=False, null=False, max_length=100)
    # icon = models.ImageField()

    def __str__(self) -> str:
        return f'{self.code} - {self.title}'


class Project(BaseModel):
    code = models.CharField(blank=False, null=False, max_length=10, unique=True)
    title = models.CharField(blank=False, null=False, max_length=100)
    description = models.TextField(blank=True, null=True)
    language = models.ManyToManyField(Language, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.code} - {self.title}'


class TranslationKey(BaseModel):
    key = models.CharField(blank=False, null=False, max_length=100)
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE,
                                related_name='project_translation_key')
    
    def __str__(self) -> str:
        return f'{self.key}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['key', 'project'], name='translate_key_unique_project')
        ]



class Translate(BaseModel):
    translate = models.CharField(blank=True, null=False, max_length=255)
    language = models.ForeignKey(Language, blank=False, null=False, on_delete=models.CASCADE,
                                related_name='language_project')
    translation_key = models.ForeignKey(TranslationKey, blank=False, null=False, on_delete=models.CASCADE,
                                related_name='translation_key_translate')
    
    def __str__(self) -> str:
        return f'{self.translation_key.key} - {self.language.code}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['language', 'translation_key'], name='translate_unique_translation_key_per_language')
        ]

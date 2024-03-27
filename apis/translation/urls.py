from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.translation.views.v1 import language, project, translate, translation_key


routers = DefaultRouter()

routers.register(r'languages', language.LanguageViewset)
routers.register(r'project', project.ProjectViewset)
routers.register(r'translate', translate.TranslateViewset)
routers.register(r'translation_key', translation_key.TranslationKeyViewset)

api_v1_urls = (routers.urls, 'v1')

app_name = 'translation'

urlpatterns = [
    path('v1/', include(api_v1_urls)),
]


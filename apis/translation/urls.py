from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.translation.views.v1 import language, project, translate, translation_key


routers = DefaultRouter()

routers.register(r'languages', language.LanguageViewset)
routers.register(r'projects', project.ProjectViewset)
routers.register(r'translates', translate.TranslateViewset)
routers.register(r'translation_keys', translation_key.TranslationKeyViewset)

api_v1_urls = (routers.urls, 'v1')

app_name = 'translation'

urlpatterns = [
    path('v1/', include(api_v1_urls)),
]


import os
from distutils.util import strtobool
from corsheaders.defaults import default_headers

CORS_ALLOWED_ORIGIN_REGEXES=os.getenv('CORS_ALLOWED_ORIGIN_REGEXES', '').split(',')
CORS_ALLOW_ALL_ORIGINS=bool(strtobool(os.getenv('CORS_ALLOW_ALL_ORIGINS', 'True')))
CUSTOM_HEADERS=os.getenv('CUSTOM_HEADERS', '').split(',')

CORS_ALLOW_HEADERS = (
    *default_headers,
    *CUSTOM_HEADERS
)

CSRF_TRUSTED_ORIGINS = os.getenv('', 'localhsot').split(',')

__all__ = [
    CORS_ALLOWED_ORIGIN_REGEXES,
    CORS_ALLOW_ALL_ORIGINS,
    CORS_ALLOW_HEADERS,
    # CSRF_TRUSTED_ORIGINS,
]
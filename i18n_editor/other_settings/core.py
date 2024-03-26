import os
from corsheaders.defaults import default_headers

CORS_ALLOWED_ORIGIN_REGEXES=''
CORS_ALLOW_ALL_ORIGINS=True

CORS_ALLOW_HEADERS = (
    *default_headers,
)

CSRF_TRUSTED_ORIGINS = os.getenv('', 'localhsot').split(',')

__all__ = [
    CORS_ALLOWED_ORIGIN_REGEXES,
    CORS_ALLOW_ALL_ORIGINS,
    CORS_ALLOW_HEADERS,
    # CSRF_TRUSTED_ORIGINS,
]
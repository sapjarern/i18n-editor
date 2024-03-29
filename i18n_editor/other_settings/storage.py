import os


STORAGES = {
    "default": {
        "BACKEND": "i18n_editor.extension.custom_storages.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "i18n_editor.extension.custom_storages.StaticStorage",
    },
}


__all__ = [
    'STORAGES',
    'AWS_S3_ACCESS_KEY_ID',
    'AWS_S3_SECRET_ACCESS_KEY',
    'AWS_STORAGE_BUCKET_NAME',
    'AWS_S3_REGION_NAME',
    'AWS_S3_CUSTOM_DOMAIN'
]

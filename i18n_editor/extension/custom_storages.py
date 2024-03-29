from storages.backends.s3boto3 import S3Boto3Storage

from i18n_editor.other_settings.storage import AWS_STORAGE_BUCKET_NAME


class MediaStorage(S3Boto3Storage):
    bucket_name = AWS_STORAGE_BUCKET_NAME
    location = 'media'


class StaticStorage(S3Boto3Storage):
    bucket_name = AWS_STORAGE_BUCKET_NAME
    location = 'static'

from typing import Any

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class CustomS3Boto3Storage(S3Boto3Storage):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        if settings.MINIO_ACCESS_URL:
            self.secure_urls = False
            self.custom_domain = settings.MINIO_ACCESS_URL

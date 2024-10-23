from django.conf import settings
from django.core.handlers.asgi import ASGIRequest


def allauth_settings(request: ASGIRequest) -> dict:
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }

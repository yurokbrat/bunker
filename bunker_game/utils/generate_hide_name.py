from uuid import uuid4

from django.db.models import Model


def upload_to_avatars(instance: Model, filename: str) -> str:
    return f"user-avatars/{uuid4().hex}"


def upload_to_catastrophes(instance: Model, filename: str) -> str:
    return f"catastrophes/{uuid4().hex}"


def upload_to_bunkers(instance: Model, filename: str) -> str:
    return f"bunkers/{uuid4().hex}"

from uuid import uuid4


def upload_to_avatars(instance, filename) -> str:
    return f"user-avatars/{uuid4().hex}"


def upload_to_catastrophes(instance, filename) -> str:
    return f"catastrophes/{uuid4().hex}"


def upload_to_bunkers(instance, filename) -> str:
    return f"bunkers/{uuid4().hex}"

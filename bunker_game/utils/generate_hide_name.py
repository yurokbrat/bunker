from uuid import uuid4


def upload_to_avatars() -> str:
    return f"user-avatars/{uuid4().hex}"


def upload_to_catastrophes() -> str:
    return f"catastrophes/{uuid4().hex}"


def upload_to_bunkers() -> str:
    return f"bunkers/{uuid4().hex}"

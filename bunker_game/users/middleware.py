from collections.abc import Callable

from django.core.handlers.asgi import ASGIRequest
from django.utils import timezone
from requests import Response

from bunker_game.users.models import User


class UpdateLastOnlineMiddleware:
    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: ASGIRequest) -> Response:
        assert hasattr(
            request,
            "user",
        ), (
            "The UpdateLastOnlineMiddleware requires "
            "authentication middleware to be installed."
        )
        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id).update(last_online=timezone.now())

        return self.get_response(request)

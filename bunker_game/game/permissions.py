from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from bunker_game.game.models import Game, Personage


class IsGameCreator(IsAuthenticated):
    def has_object_permission(self, request: Request, view: APIView, obj: Game) -> bool:
        return obj.creator == request.user


class IsRelatedPersonage(IsAuthenticated):
    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: Personage,
    ) -> bool:
        return obj.user == request.user

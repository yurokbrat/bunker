from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from bunker_game.game.models import Game, Personage
from bunker_game.game.models.vote import Voting


class IsUserGameCreator(IsAuthenticated):
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


class IsUserGamePersonage(IsAuthenticated):
    def has_object_permission(self, request: Request, view: APIView, obj: Game) -> bool:
        return any(request.user == personage.user for personage in obj.personages.all())


class IsUserVotingPersonage(IsAuthenticated):
    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: Voting,
    ) -> bool:
        return any(
            request.user == personage.user for personage in obj.game.personages.all()
        )

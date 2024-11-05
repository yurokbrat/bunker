from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from bunker_game.game.models import Game, Personage
from bunker_game.game.models.vote import Vote, Voting


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


class IsRelatedVoter(IsAuthenticated):
    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: Vote | Voting,
    ) -> bool:
        if isinstance(obj, Vote):
            return any(
                request.user == personage.user
                for personage in obj.voting.game.personages.all()
            )
        return any(
            request.user == personage.user for personage in obj.game.personages.all()
        )


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


class IsUserVotingCreatorGame(IsAuthenticated):
    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: Voting,
    ) -> bool:
        return obj.game.creator == request.user

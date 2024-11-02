from typing import Any

from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import Game
from bunker_game.game.models.vote import Voting
from bunker_game.game.permissions import IsUserVotingCreatorGame, IsUserVotingPersonage
from bunker_game.game.serializers.personage_serializers import PersonageShortSerializer
from bunker_game.game.serializers.vote_serializers import (
    GiveVoiceSerializer,
    ResultVotingSerializer,
    VoteSerializer,
    VotingSerializer,
)
from bunker_game.game.services.vote_service import VoteService
from bunker_game.utils.exceptions import UserNotCreatorGameError
from bunker_game.utils.mixins import PermissionByActionMixin, WebSocketMixin


class VoteViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    WebSocketMixin,
    PermissionByActionMixin,
    viewsets.GenericViewSet,
):
    queryset = Voting.objects.all()  # type: ignore[attr-defined]
    serializer_class = VotingSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_action_classes = {
        "list": IsUserVotingPersonage,
        "retrieve": IsUserVotingPersonage,
        "vote": IsUserVotingPersonage,
        "start": IsUserVotingPersonage,
        "stop": IsUserVotingCreatorGame,
    }
    filterset_fields = ("is_active",)
    lookup_field = "uuid"
    lookup_url_kwarg = "voting_uuid"

    def get_queryset(self) -> QuerySet[Voting]:
        if game_uuid := self.kwargs.get("game_uuid"):
            return Voting.objects.filter(game__uuid=game_uuid)  # type: ignore[attr-defined]
        return Voting.objects.none()  # type: ignore[attr-defined]

    @extend_schema(request=None, responses=VotingSerializer())
    @action(detail=False, methods=("POST",))
    def start(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game_uuid = self.kwargs.get("game_uuid")
        game = get_object_or_404(Game, uuid=game_uuid)
        if game.creator != request.user:
            raise UserNotCreatorGameError
        voting = VoteService().start(game)
        voting_data = VotingSerializer(
            instance=voting,
            context={"request": request},
        ).data
        self.web_socket_start_voting(game.uuid, voting_data)
        return Response(data=voting_data, status=status.HTTP_200_OK)

    @extend_schema(request=GiveVoiceSerializer(), responses=VoteSerializer())
    @action(detail=True, methods=("POST",), serializer_class=GiveVoiceSerializer)
    def vote(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        voting = self.get_object()
        target_uuid = serializer.validated_data["target"]
        vote = VoteService().vote(voting, request.user, target_uuid)  # type: ignore[arg-type]
        voting_data = VoteSerializer(instance=vote, context={"request": request}).data
        self.web_socket_send_vote(voting.game.uuid, voting_data)
        return Response(data=voting_data, status=status.HTTP_201_CREATED)

    @extend_schema(request=None, responses=ResultVotingSerializer())
    @action(detail=True, methods=("POST",))
    def stop(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        voting = self.get_object()
        personage, vote_count = VoteService().stop(voting)
        personage_serializer = PersonageShortSerializer(
            personage,
            context={"request": request},
        )
        results_data = {
            "results": {
                "personage": personage_serializer.data,
                "vote_count": vote_count,
            },
        }
        self.web_socket_stop_voting(voting.game.uuid, results_data)
        return Response(data=results_data, status=status.HTTP_201_CREATED)

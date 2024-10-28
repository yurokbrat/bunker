from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import Personage
from bunker_game.game.models.game import Game
from bunker_game.game.serializers import (
    GameSerializer,
    NewGameSerializer,
)
from bunker_game.game.services import GenerateGameService
from bunker_game.utils.websocket_mixin import WebSocketMixin


class GameViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    WebSocketMixin,
    viewsets.GenericViewSet,
):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_url_kwarg = "game_uuid"
    lookup_field = "uuid"
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("personages__uuid",)
    filterset_fields = ("is_active", "date_start")

    @extend_schema(responses=GameSerializer())
    @action(
        detail=False,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=NewGameSerializer,
    )
    def new(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game = Game.objects.create(
            creator=request.user,  # type: ignore[misc]
            game_duration_type=serializer.validated_data["game_duration_type"],
        )
        serializer = GameSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(request=None, responses=GameSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
    )
    def start(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game: Game = self.get_object()
        if game.is_active:
            return Response(data="Игра уже начата", status=status.HTTP_400_BAD_REQUEST)
        GenerateGameService()(game)
        serializer = GameSerializer(instance=game, context={"request": request})
        self.start_game(game.uuid, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=None, responses=GameSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=GameSerializer,
    )
    def connect(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game = self.get_object()
        personage, created = Personage.objects.get_or_create(
            user=request.user,
            game_id=game.id,
        )
        if created:
            game.personages.add(personage)
            game.save()
            self.join_game(game.uuid, personage, request)
        serializer = GameSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance: Game) -> None:
        # TODO: Сделать заморозку игры на сутки
        super().perform_destroy(instance)

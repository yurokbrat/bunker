from typing import Any

from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import Personage
from bunker_game.game.models.game import Game
from bunker_game.game.permissions import IsUserGameCreator, IsUserGamePersonage
from bunker_game.game.serializers import (
    GameRetrieveSerializer,
    KickPersonageGameSerializer,
    NewGameSerializer,
)
from bunker_game.game.serializers.game_serializers import (
    GameListSerializer,
    GameShortSerializer,
)
from bunker_game.game.services import GenerateGameService
from bunker_game.utils.exceptions import GameActiveError
from bunker_game.utils.mixins import (
    PermissionByActionMixin,
    SerializerByActionMixin,
    WebSocketMixin,
)


class GameViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    WebSocketMixin,
    PermissionByActionMixin,
    SerializerByActionMixin,
    viewsets.GenericViewSet,
):
    queryset = Game.objects.all()
    serializer_class = GameRetrieveSerializer
    serializer_action_classes = {
        "list": GameListSerializer,
        "retrieve": GameRetrieveSerializer,
        "new": NewGameSerializer,
        "connect": GameShortSerializer,
        "kick": KickPersonageGameSerializer,
    }
    permission_action_classes = {
        "start": IsUserGameCreator,
        "stop": IsUserGameCreator,
        "destroy": IsUserGameCreator,
        "kick": IsUserGameCreator,
        "disconnect": IsUserGamePersonage,
        "list": IsUserGamePersonage,
        "retrieve": IsUserGamePersonage,
        "connect": IsAuthenticated,
    }
    lookup_url_kwarg = "uuid"
    lookup_field = "uuid"
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("personages__uuid",)
    filterset_fields = ("is_active", "date_start")

    @extend_schema(responses=GameRetrieveSerializer())
    @action(detail=False, methods=("POST",))
    def new(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game = Game.objects.create(
            creator=request.user,  # type: ignore[misc]
            game_duration_type=serializer.validated_data["game_duration_type"],
        )
        serializer = GameRetrieveSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(request=None, responses=GameRetrieveSerializer())
    @action(detail=True, methods=("POST",))
    def start(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game = self.get_object()
        if game.is_active:
            raise GameActiveError
        GenerateGameService()(game)
        serializer = GameRetrieveSerializer(instance=game, context={"request": request})
        self.web_socket_start_game(game.uuid, serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=None, responses=None)
    @action(detail=True, methods=("POST",))
    def stop(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game = self.get_object()
        game.is_active = False
        game.date_end = timezone.now()
        game.save()
        serializer = GameRetrieveSerializer(instance=game, context={"request": request})
        self.web_socket_stop_game(game.uuid, serializer.data)
        return Response(data="Игра завершена", status=status.HTTP_200_OK)

    @extend_schema(request=None, responses=GameRetrieveSerializer())
    @action(detail=True, methods=("POST",))
    def connect(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game = self.get_object()
        personage, created = Personage.objects.get_or_create(
            user=request.user,
            game_id=game.id,
        )
        if created:
            game.personages.add(personage)
            game.save()
            self.web_socket_join_game(game.uuid, personage, request)
        serializer = GameRetrieveSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(request=None, responses=None)
    @action(detail=True, methods=("DELETE",))
    def disconnect(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game = self.get_object()
        personage = get_object_or_404(
            Personage,
            game_id=game.id,
        )
        self.web_socket_exit_game(game.uuid, personage, request)
        personage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses=None)
    @action(detail=True, methods=("POST",))
    def kick(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        game = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        personage_uuid = serializer.validated_data["personage_uuid"]
        personage = get_object_or_404(Personage, uuid=personage_uuid)
        personage.delete()
        self.web_socket_kick_personage(game.uuid, personage, request)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance: Game) -> None:
        # TODO: Сделать заморозку игры на сутки
        super().perform_destroy(instance)

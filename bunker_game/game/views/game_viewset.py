from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import Personage
from bunker_game.game.models.game import Game
from bunker_game.game.serializers.game_serializers import GameSerializer
from bunker_game.game.services.generate_game_service import GenerateGameService


class GameViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_url_kwarg = "id"

    @extend_schema(responses=GameSerializer())
    @action(
        detail=False,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=None,
    )
    def new(self, request, *args, **kwargs):
        game = Game.objects.create(creator=request.user)
        serializer = GameSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(responses=GameSerializer())
    @action(detail=False, methods=("GET",), permission_classes=(IsAuthenticated,))
    def live(self, request, *args, **kwargs):
        live_games = Game.objects.filter(is_active=True)
        serializer = GameSerializer(
            instance=live_games, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(responses=GameSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=None,
    )
    def start(self, request, *args, **kwargs):
        game = self.get_object()
        GenerateGameService()(game.id)
        serializer = GameSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(responses=GameSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=None,
    )
    def connect(self, request, *args, **kwargs):
        game = self.get_object()
        personage = Personage.objects.create(user=request.user)
        game.personages.add(personage)
        game.save()
        serializer = GameSerializer(instance=game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(
        detail=True,
        methods=("DELETE",),
        permission_classes=(IsAuthenticated,),
        serializer_class=None,
    )
    def stop(self, request: Request, *args, **kwargs):
        game = self.get_object()
        # TODO: Сделать заморозку игры на сутки
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO: сделать через id карты действия действие
    # @action(
    #     detail=True,
    #     methods=("POST",),
    #     permission_classes=(IsAuthenticated,),
    #     serializer_class=None,
    # )
    # def use_action_card(self, request: Request, *args, **kwargs):


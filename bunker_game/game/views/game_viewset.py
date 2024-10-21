from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import Personage
from bunker_game.game.models.game import Game
from bunker_game.game.models.use_action_card import ActionCardUsage
from bunker_game.game.serializers.action_card_serializers import UseActionCardSerializer
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
            instance=live_games,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(request=None, responses=GameSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=GameSerializer,
    )
    def start(self, request, *args, **kwargs):
        game = self.get_object()
        if game.is_active:
            return Response(data="Игра уже начата", status=status.HTTP_400_BAD_REQUEST)
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
        personage, created = Personage.objects.get_or_create(
            user=request.user,
            game_id=game.id,
        )
        if created:
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

    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=UseActionCardSerializer,
        url_path="use-action-card",
    )
    def use_action_card(self, request: Request, *args, **kwargs):
        action_card = get_object_or_404(ActionCardUsage, card__key=request.data["key"])
        action_card.is_used = True
        action_card.save()
        return Response({"is_used": action_card.is_used}, status=status.HTTP_200_OK)

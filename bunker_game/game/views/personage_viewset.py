from typing import Any

from django.db.models import Model, QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.constants import DEFAULT_CHARACTERISTICS
from bunker_game.game.models import CharacteristicVisibility, Personage
from bunker_game.game.serializers import (
    ActionCardUsageSerializer,
    CharacteristicVisibilitySerializer,
    PersonageRegenerateSerializer,
    PersonageSerializer,
    UseActionCardSerializer,
)
from bunker_game.game.services import (
    GeneratePersonageService,
    RegenerateCharacteristicService,
    UseActionCardService,
)
from bunker_game.utils.format_characteristic_value_mixin import (
    FormatCharacteristicValueMixin,
)
from bunker_game.utils.websocket_mixin import WebSocketMixin


class PersonageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    WebSocketMixin,
    FormatCharacteristicValueMixin,
    viewsets.GenericViewSet,
):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer
    lookup_url_kwarg = "personage_uuid"
    lookup_field = "uuid"

    def get_queryset(self) -> QuerySet[Personage]:
        return Personage.objects.all()

    @extend_schema(request=None, responses=PersonageSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
    )
    def generate(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        personage = self.get_object()
        new_personage, created = GeneratePersonageService()(personage)
        personage_serializer = PersonageSerializer(
            instance=new_personage,
            context={"request": request},
        )
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(personage_serializer.data, status=status_code)

    @action(
        detail=True,
        methods=("PATCH",),
        permission_classes=(IsAuthenticated,),
        serializer_class=PersonageRegenerateSerializer,
    )
    def regenerate(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        regenerate_serializer = PersonageRegenerateSerializer(data=request.data)
        regenerate_serializer.is_valid(raise_exception=True)
        characteristic = regenerate_serializer.validated_data["characteristic_type"]
        personage = self.get_object()
        new_characteristic = RegenerateCharacteristicService()(
            personage,
            characteristic,
        )
        if isinstance(new_characteristic, Model):
            serializer = self.format_characteristic_value(
                characteristic,
                new_characteristic,
                request,
            )
            return Response(
                {characteristic: serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response({characteristic: new_characteristic}, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=("PATCH",),
        permission_classes=(IsAuthenticated,),
        serializer_class=CharacteristicVisibilitySerializer,
        url_path="reveal-characteristic",
    )
    def reveal_characteristic(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        personage = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        characteristic_type = serializer.validated_data["characteristic_type"]
        if characteristic_type not in DEFAULT_CHARACTERISTICS:
            error_message = "Invalid characteristic"
            raise ValidationError(error_message)
        visibility, _ = CharacteristicVisibility.objects.get_or_create(
            personage=personage,
            characteristic_type=characteristic_type,
        )
        visibility.is_hidden = False
        visibility.save()
        characteristic_value = getattr(personage, characteristic_type)
        if isinstance(characteristic_value, Model):
            characteristic_value = self.format_characteristic_value(
                characteristic_type,
                characteristic_value,
                request,
            ).data
        self.web_socket_send_characteristic(
            personage.game.uuid,
            personage.id,
            characteristic_type,
            characteristic_value,
        )

        return Response(
            {
                "characteristic_type": characteristic_type,
                "characteristic_value": characteristic_value,
                "is_hidden": False,
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=UseActionCardSerializer(),
        responses=ActionCardUsageSerializer(),
    )
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(IsAuthenticated,),
        serializer_class=UseActionCardSerializer,
        url_path="use-action-card",
    )
    def use_action_card(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        personage = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        action_card = UseActionCardService()(
            card_key=serializer.validated_data["key"],
            game=personage.game,
            target_uuid=serializer.validated_data.get("target_uuid"),
            personage_instance=personage,
            showing_characteristic_type=serializer.validated_data.get(
                "showing_characteristic_type",
            ),
        )
        action_serializer = ActionCardUsageSerializer(
            instance=action_card,
            context={"request": request},
        )
        self.web_socket_send_action_card(personage.game.uuid, action_card, request)
        return Response(action_serializer.data, status=status.HTTP_200_OK)

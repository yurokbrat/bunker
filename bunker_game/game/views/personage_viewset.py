from typing import Any

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Model, QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import CharacteristicVisibility, Personage
from bunker_game.game.serializers import PersonageSerializer
from bunker_game.game.serializers.action_card_serializers import (
    ActionCardSerializer,
    ActionCardUsageSerializer,
    UseActionCardSerializer,
)
from bunker_game.game.serializers.personage_serializers import (
    AdditionalInfoSerializer,
    BaggageSerializer,
    CharacteristicVisibilitySerializer,
    CharacterSerializer,
    DiseaseSerializer,
    HobbySerializer,
    PersonageRegenerateSerializer,
    PhobiaSerializer,
    ProfessionSerializer,
)
from bunker_game.game.services.generate_personage_service import (
    GeneratePersonageService,
)
from bunker_game.game.services.regenerate_action_card_service import (
    RegenerateActionCardService,
)
from bunker_game.game.services.regenerate_characteristic_service import (
    RegenerateCharacteristicService,
)
from bunker_game.game.services.use_action_card_service import UseActionCardService


class PersonageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer
    lookup_url_kwarg = "personage_uuid"
    lookup_field = "uuid"

    def get_queryset(self) -> QuerySet[Personage]:
        if game_uuid := self.kwargs.get("game_uuid"):
            return Personage.objects.filter(games__uuid=game_uuid)
        return Personage.objects.none()

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
            serializers_map = {
                "disease": DiseaseSerializer,
                "profession": ProfessionSerializer,
                "phobia": PhobiaSerializer,
                "hobby": HobbySerializer,
                "character": CharacterSerializer,
                "additional_info": AdditionalInfoSerializer,
                "baggage": BaggageSerializer,
            }
            serializer_type = serializers_map[characteristic]
            serializer = serializer_type(
                instance=new_characteristic,
                context={"request": request},
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
        url_path="regenerate-action-card",
        serializer_class=None,
    )
    def regenerate_action_card(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        personage = self.get_object()
        new_action_card = RegenerateActionCardService()(personage)
        action_card_serializer = ActionCardSerializer(
            instance=new_action_card,
            context={"request": request},
        )

        return Response(
            {"New action card": action_card_serializer.data},
            status=status.HTTP_200_OK,
        )

    @action(
        detail=True,
        methods=("PATCH",),
        permission_classes=(IsAuthenticated,),
        serializer_class=CharacteristicVisibilitySerializer,
    )
    def toggle_visibility(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        game_uuid = self.kwargs.get("game_uuid")
        personage = self.get_object()
        characteristic_type = request.data.get("characteristic_type")
        is_hidden = request.data.get("is_hidden")
        visibility, _ = CharacteristicVisibility.objects.get_or_create(
            personage=personage,
            characteristic_type=characteristic_type,
        )
        visibility.is_hidden = is_hidden  # type: ignore[assignment]
        visibility.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_uuid}",
            {
                "type": "update_characteristics",
                "personage_id": personage.id,
                "characteristic_type": characteristic_type,
                "is_hidden": is_hidden,
            },
        )

        return Response(
            {"characteristic_type": characteristic_type, "is_hidden": is_hidden},
            status=status.HTTP_200_OK,
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
        return Response(action_serializer.data, status=status.HTTP_200_OK)

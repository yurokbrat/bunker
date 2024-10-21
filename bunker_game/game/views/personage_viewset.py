from typing import Any

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Model, QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import CharacteristicVisibility, Personage
from bunker_game.game.serializers import PersonageSerializer
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
from bunker_game.game.services.regenerate_characteristic_service import (
    RegenerateCharacteristicService,
)


class PersonageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer
    lookup_url_kwarg = "personage_id"

    def get_queryset(self) -> QuerySet:
        game_id = self.kwargs.get("game_id")
        return Personage.objects.filter(games=game_id)

    @extend_schema(request=None, responses=PersonageSerializer())
    @action(
        detail=True,
        methods=("POST",),
        permission_classes=(permissions.IsAuthenticated,),
        serializer_class=PersonageSerializer,
    )
    def generate(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        personage = self.get_object()
        personage, created = GeneratePersonageService()(personage.id)
        personage_serializer = PersonageSerializer(
            instance=personage,
            context={"request": request},
        )
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(personage_serializer.data, status=status_code)

    @action(
        detail=True,
        methods=("PATCH", "PUT"),
        permission_classes=(permissions.IsAuthenticated,),
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
            serializer = serializers_map.get(characteristic)
            new_characteristic = serializer(
                instance=new_characteristic,
                context={"request": request},
            )
            return Response(
                {characteristic: new_characteristic.data},
                status=status.HTTP_200_OK,
            )
        return Response({characteristic: new_characteristic}, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["PATCH"],
        permission_classes=(permissions.IsAuthenticated,),
        serializer_class=CharacteristicVisibilitySerializer,
    )
    def toggle_visibility(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        game_id = self.kwargs.get("game_id")
        personage = self.get_object()
        characteristic_type = request.data.get("characteristic_type")
        is_hidden = request.data.get("is_hidden")
        visibility, _ = CharacteristicVisibility.objects.get_or_create(
            personage=personage,
            characteristic_type=characteristic_type,
        )
        visibility.is_hidden = is_hidden
        visibility.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_id}",
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

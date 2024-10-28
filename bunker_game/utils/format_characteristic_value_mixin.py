from django.db.models import Model
from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer

from bunker_game.game.serializers import (
    AdditionalInfoSerializer,
    BaggageSerializer,
    CharacterSerializer,
    DiseaseSerializer,
    HobbySerializer,
    PhobiaSerializer,
    ProfessionSerializer,
)


class FormatCharacteristicValueMixin:
    def format_characteristic_value(
        self,
        characteristic_type: str,
        characteristic_value: Model,
        request: Request,
    ) -> ModelSerializer:
        serializers_map = {
            "disease": DiseaseSerializer,
            "profession": ProfessionSerializer,
            "phobia": PhobiaSerializer,
            "hobby": HobbySerializer,
            "character": CharacterSerializer,
            "additional_info": AdditionalInfoSerializer,
            "baggage": BaggageSerializer,
        }
        serializer_type = serializers_map[characteristic_type]
        return serializer_type(
            instance=characteristic_value,
            context={"request": request},
        )

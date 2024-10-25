from typing import Any

from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from bunker_game.game.constants import ActionCardTargetChoice, GameDurationType
from bunker_game.game.models.game import Game
from bunker_game.game.serializers import (
    ActionCardSerializer,
    BunkerSerializer,
    CatastropheSerializer,
)
from bunker_game.game.serializers.personage_serializers import PersonageSerializer
from bunker_game.users.serializers import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    personages = PersonageSerializer(many=True, read_only=True, allow_null=True)
    bunker = BunkerSerializer()
    catastrophe = CatastropheSerializer()
    used_action_cards = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = (
            "uuid",
            "creator",
            "personages",
            "bunker",
            "catastrophe",
            "num_places",
            "game_duration_type",
            "time_in_bunker",
            "used_action_cards",
            "date_start",
            "date_end",
            "is_active",
        )

    @extend_schema_field(ActionCardSerializer())
    def get_used_action_cards(self, obj: Game) -> dict[str, Any]:
        used_action_card_usages = obj.action_cards.filter(
            is_used=True,
            card__target__in=(ActionCardTargetChoice.ALL, ActionCardTargetChoice.GAME),
        )
        used_action_cards = [usage.card for usage in used_action_card_usages]
        return ActionCardSerializer(used_action_cards, many=True).data


class NewGameSerializer(serializers.Serializer):
    game_duration_type = serializers.ChoiceField(
        GameDurationType.choices,
        default=GameDurationType.MEDIUM,
    )

from rest_framework import serializers

from bunker_game.game.enums import GameDurationType
from bunker_game.game.models.game import Game
from bunker_game.game.serializers import (
    ActionCardUsageSerializer,
    BunkerSerializer,
    CatastropheSerializer,
)
from bunker_game.game.serializers.personage_serializers import (
    PersonageSerializer,
)
from bunker_game.users.serializers import UserShortSerializer


class GameSerializer(serializers.ModelSerializer):
    creator = UserShortSerializer(read_only=True)
    personages = PersonageSerializer(many=True, read_only=True, allow_null=True)
    bunker = BunkerSerializer()
    catastrophe = CatastropheSerializer()
    action_cards = ActionCardUsageSerializer(many=True)

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
            "action_cards",
            "date_start",
            "date_end",
            "is_active",
        )


class NewGameSerializer(serializers.Serializer):
    game_duration_type = serializers.ChoiceField(
        GameDurationType.choices,
        default=GameDurationType.MEDIUM,
    )

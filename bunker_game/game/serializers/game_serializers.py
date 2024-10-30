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
    PersonageShortSerializer,
)
from bunker_game.users.serializers import UserShortSerializer


class GameShortSerializer(serializers.ModelSerializer):
    creator = UserShortSerializer(read_only=True)
    personages = PersonageShortSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Game
        fields: tuple[str, ...] = (
            "uuid",
            "creator",
            "personages",
        )


class GameSerializer(GameShortSerializer):
    personages = PersonageSerializer(many=True, read_only=True, allow_null=True)
    bunker = BunkerSerializer()
    catastrophe = CatastropheSerializer()
    action_cards = ActionCardUsageSerializer(many=True)

    class Meta(GameShortSerializer.Meta):
        fields = (
            *GameShortSerializer.Meta.fields,
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


class KickPersonageGameSerializer(serializers.Serializer):
    personage_uuid = serializers.UUIDField(write_only=True)

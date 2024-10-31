from rest_framework import serializers

from bunker_game.game.enums import GameDurationType
from bunker_game.game.models.game import Game
from bunker_game.game.serializers import (
    ActionCardUsageSerializer,
    BunkerRetrieveSerializer,
    CatastropheRetrieveSerializer,
)
from bunker_game.game.serializers.bunker_serializers import BunkerListSerializer
from bunker_game.game.serializers.catastrophe_serializers import (
    CatastropheListSerializer,
)
from bunker_game.game.serializers.personage_serializers import (
    PersonageRetrieveSerializer,
    PersonageShortSerializer,
)
from bunker_game.users.serializers import UserShortSerializer


class GameShortSerializer(serializers.ModelSerializer):
    creator = UserShortSerializer(read_only=True)
    personages_count = serializers.SerializerMethodField(read_only=True)
    personages = PersonageShortSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Game
        fields: tuple[str, ...] = (
            "uuid",
            "creator",
            "personages_count",
            "personages",
        )

    def get_personages_count(self, obj: Game) -> int:
        return obj.personages.count()


class GameListSerializer(GameShortSerializer):
    bunker = BunkerListSerializer()
    catastrophe = CatastropheListSerializer()

    class Meta(GameShortSerializer.Meta):
        fields = (
            *GameShortSerializer.Meta.fields,
            "bunker",
            "catastrophe",
            "is_active",
        )


class GameRetrieveSerializer(GameListSerializer):
    personages = PersonageRetrieveSerializer(many=True, read_only=True, allow_null=True)
    bunker = BunkerRetrieveSerializer()
    catastrophe = CatastropheRetrieveSerializer()
    action_cards = ActionCardUsageSerializer(many=True)

    class Meta(GameListSerializer.Meta):
        fields = (
            *GameListSerializer.Meta.fields,
            "personages",
            "num_places",
            "game_duration_type",
            "time_in_bunker",
            "action_cards",
            "date_start",
            "date_end",
        )


class NewGameSerializer(serializers.Serializer):
    game_duration_type = serializers.ChoiceField(
        GameDurationType.choices,
        default=GameDurationType.MEDIUM,
    )


class KickPersonageGameSerializer(serializers.Serializer):
    personage_uuid = serializers.UUIDField(write_only=True)

from rest_framework import serializers

from bunker_game.game.models.game import Game
from bunker_game.game.serializers import BunkerSerializer, PersonageSerializer
from bunker_game.game.serializers.catastrophe_serializers import CatastropheSerializer
from bunker_game.users.serializers import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    personages = PersonageSerializer(many=True, read_only=True, allow_null=True)
    bunker = BunkerSerializer()
    catastrophe = CatastropheSerializer()

    class Meta:
        model = Game
        fields = (
            "id",
            "creator",
            "personages",
            "bunker",
            "catastrophe",
            "date_start",
            "date_end",
            "is_active",
        )

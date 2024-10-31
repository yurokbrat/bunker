from rest_framework import serializers

from bunker_game.game.models import Bunker, BunkerRoom


class BunkerRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BunkerRoom
        fields = ("uuid", "name", "area")


class BunkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bunker
        fields: tuple[str, ...] = ("uuid", "name", "image")


class BunkerRetrieveSerializer(BunkerListSerializer):
    rooms = BunkerRoomsSerializer(many=True)

    class Meta(BunkerListSerializer.Meta):
        fields = (*BunkerListSerializer.Meta.fields, "description", "rooms")

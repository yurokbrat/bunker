from rest_framework import serializers

from bunker_game.game.models import Bunker, BunkerRoom


class BunkerRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BunkerRoom
        fields = ("uuid", "name", "area")


class BunkerSerializer(serializers.ModelSerializer):
    rooms = BunkerRoomsSerializer(many=True)

    class Meta:
        model = Bunker
        fields = ("uuid", "name", "description", "image", "rooms")

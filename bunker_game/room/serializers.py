from rest_framework import serializers

from bunker_game.room.models import Room
from bunker_game.users.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ("id", "creator", "is_started", "date_start")

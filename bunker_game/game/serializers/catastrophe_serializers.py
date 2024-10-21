from rest_framework import serializers

from bunker_game.game.models import Catastrophe


class CatastropheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catastrophe
        fields = ("id", "uuid", "name", "description", "image", "impact_level")

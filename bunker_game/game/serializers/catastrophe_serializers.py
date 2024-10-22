from rest_framework import serializers

from bunker_game.game.models import Catastrophe


class CatastropheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catastrophe
        fields = (
            "uuid",
            "name",
            "description",
            "image",
            "percent_population",
            "impact_level",
        )

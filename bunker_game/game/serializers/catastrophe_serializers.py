from rest_framework import serializers

from bunker_game.game.models import Catastrophe


class CatastropheListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catastrophe
        fields: tuple[str, ...] = (
            "uuid",
            "name",
            "image",
            "impact_level",
        )


class CatastropheRetrieveSerializer(CatastropheListSerializer):
    class Meta(CatastropheListSerializer.Meta):
        fields = (
            *CatastropheListSerializer.Meta.fields,
            "description",
            "percent_population",
        )

from rest_framework import serializers

from bunker_game.game.models.action_card import ActionCard
from bunker_game.game.models.use_action_card import ActionCardUsage


class ActionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionCard
        fields = ("name", "key", "description", "target")
        read_only_fields = ("name", "key", "description", "target")


class UseActionCardSerializer(serializers.ModelSerializer):
    card_key = serializers.SlugField()
    personage_id = serializers.IntegerField()

    class Meta:
        model = ActionCardUsage
        fields = ("card_key", "personage_id")

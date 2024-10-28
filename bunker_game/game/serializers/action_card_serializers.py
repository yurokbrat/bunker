from rest_framework import serializers

from bunker_game.game.enums import TypeCharacteristic
from bunker_game.game.models import ActionCard, ActionCardUsage


class ActionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionCard
        fields = ("uuid", "name", "key", "description", "target")
        read_only_fields = ("name", "key", "description", "target")


class ActionCardUsageSerializer(serializers.ModelSerializer):
    card = ActionCardSerializer()

    class Meta:
        model = ActionCardUsage
        fields: tuple[str, ...] = ("uuid", "card", "is_used")


class UseActionCardSerializer(serializers.Serializer):
    key = serializers.CharField(label="Уникальный ключ карты действия")
    target_uuid = serializers.UUIDField(
        label="UUID цели",
        allow_null=True,
        required=False,
    )
    showing_characteristic_type = serializers.ChoiceField(
        TypeCharacteristic.choices,
        allow_null=True,
        required=False,
        label="Характеристика, которую нужно открыть",
        help_text="Только, если карта с ключем 'show_any'",
    )

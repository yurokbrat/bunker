from rest_framework import serializers

from bunker_game.game.enums import TypeCharacteristicChoices
from bunker_game.game.models import ActionCard, ActionCardUsage


class ActionCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionCard
        fields: tuple[str, ...] = ("uuid", "name", "key")


class ActionCardRetrieveSerializer(ActionCardListSerializer):
    class Meta(ActionCardListSerializer.Meta):
        fields = (*ActionCardListSerializer.Meta.fields, "description", "target")


class ActionCardUsageSerializer(serializers.ModelSerializer):
    card = ActionCardRetrieveSerializer()

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
    characteristic_type = serializers.ChoiceField(
        choices=TypeCharacteristicChoices.choices,
        allow_null=True,
        required=False,
        label="Характеристика, которую нужно открыть",
        help_text="Только, если карта с ключем 'show_any'",
    )

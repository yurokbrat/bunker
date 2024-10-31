from rest_framework import serializers

from bunker_game.game.enums import TypeCharacteristicChoices
from bunker_game.game.models import (
    AdditionalInfo,
    Baggage,
    Character,
    CharacteristicVisibility,
    Disease,
    Hobby,
    Personage,
    Phobia,
    Profession,
)
from bunker_game.game.serializers.action_card_serializers import (
    ActionCardUsageSerializer,
)
from bunker_game.users.serializers import UserShortSerializer


class DiseaseShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields: tuple[str, ...] = ("uuid", "name")


class DiseaseSerializer(DiseaseShortSerializer):
    class Meta(DiseaseShortSerializer.Meta):
        fields = (*DiseaseShortSerializer.Meta.fields, "degree_percent", "is_curable")


class ProfessionShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields: tuple[str, ...] = ("uuid", "name")


class ProfessionSerializer(ProfessionShortSerializer):
    class Meta(ProfessionShortSerializer.Meta):
        fields = (
            *ProfessionShortSerializer.Meta.fields,
            "additional_skill",
            "experience",
        )


class PhobiaShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phobia
        fields: tuple[str, ...] = ("uuid", "name")


class PhobiaSerializer(PhobiaShortSerializer):
    class Meta(PhobiaShortSerializer.Meta):
        fields = (*PhobiaShortSerializer.Meta.fields, "stage")


class HobbyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields: tuple[str, ...] = ("uuid", "name")


class HobbySerializer(HobbyShortSerializer):
    class Meta(HobbyShortSerializer.Meta):
        fields = (*HobbyShortSerializer.Meta.fields, "experience")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("uuid", "name")


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ("uuid", "name")


class BaggageShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields: tuple[str, ...] = ("uuid", "name")


class BaggageSerializer(BaggageShortSerializer):
    class Meta(BaggageShortSerializer.Meta):
        fields = (*BaggageShortSerializer.Meta.fields, "status")


class PersonageShortSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)
    disease = DiseaseShortSerializer()
    profession = ProfessionShortSerializer()
    phobia = PhobiaShortSerializer()
    hobby = HobbyShortSerializer()
    character = CharacterSerializer()
    additional_info = AdditionalInfoSerializer()
    baggage = BaggageShortSerializer()

    class Meta:
        model = Personage
        fields: tuple[str, ...] = (
            "uuid",
            "user",
            "age",
            "gender",
            "orientation",
            "disease",
            "profession",
            "phobia",
            "hobby",
            "character",
            "additional_info",
            "baggage",
        )


class PersonageListSerializer(PersonageShortSerializer): ...


class PersonageRetrieveSerializer(PersonageListSerializer):
    disease = DiseaseSerializer()
    profession = ProfessionSerializer()
    phobia = PhobiaSerializer()
    hobby = HobbySerializer()
    baggage = BaggageSerializer()
    action_cards = ActionCardUsageSerializer(read_only=True, many=True)

    class Meta(PersonageListSerializer.Meta):
        fields = (
            *PersonageListSerializer.Meta.fields,
            "disease",
            "profession",
            "phobia",
            "hobby",
            "character",
            "additional_info",
            "baggage",
            "action_cards",
        )


class PersonageRegenerateSerializer(serializers.Serializer):
    characteristic_type = serializers.ChoiceField(
        choices=TypeCharacteristicChoices.choices,
    )


class CharacteristicVisibilitySerializer(serializers.ModelSerializer):
    characteristic_type = serializers.ChoiceField(
        choices=TypeCharacteristicChoices.choices,
    )
    is_hidden = serializers.BooleanField(read_only=True)

    class Meta:
        model = CharacteristicVisibility
        fields = ("uuid", "characteristic_type", "is_hidden")


class PersonageActionCardSerializer(ActionCardUsageSerializer):
    personage = PersonageShortSerializer(read_only=True)

    class Meta(ActionCardUsageSerializer.Meta):
        fields = (*ActionCardUsageSerializer.Meta.fields, "personage")

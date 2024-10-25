from rest_framework import serializers

from bunker_game.game.constants import TypeCharacteristic
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
from bunker_game.users.serializers import UserSerializer


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ("uuid", "name", "degree_percent", "is_curable")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("uuid", "name", "additional_skill", "experience")


class PhobiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phobia
        fields = ("uuid", "name", "stage")


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ("uuid", "name", "experience")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("uuid", "name")


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ("uuid", "name")


class BaggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ("uuid", "name", "status")


class PersonageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    disease = DiseaseSerializer()
    profession = ProfessionSerializer()
    phobia = PhobiaSerializer()
    hobby = HobbySerializer()
    character = CharacterSerializer()
    additional_info = AdditionalInfoSerializer()
    baggage = BaggageSerializer()
    action_cards = ActionCardUsageSerializer(read_only=True, many=True)

    class Meta:
        model = Personage
        fields = (
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
            "action_cards",
        )


class PersonageRegenerateSerializer(serializers.Serializer):
    characteristic_type = serializers.ChoiceField(choices=TypeCharacteristic.choices)


class CharacteristicVisibilitySerializer(serializers.ModelSerializer):
    characteristic_type = serializers.ChoiceField(choices=TypeCharacteristic.choices)

    class Meta:
        model = CharacteristicVisibility
        fields = ("uuid", "characteristic_type", "is_hidden")

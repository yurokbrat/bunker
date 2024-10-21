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
from bunker_game.users.serializers import UserSerializer


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ("id", "uuid", "name", "degree_percent", "is_curable")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "uuid", "name", "experience")


class PhobiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phobia
        fields = ("id", "uuid", "name", "stage")


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ("id", "uuid", "name", "experience")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "uuid", "name")


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ("id", "uuid", "name")


class BaggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ("id", "uuid", "name", "status")


class PersonageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    disease = DiseaseSerializer()
    profession = ProfessionSerializer()
    phobia = PhobiaSerializer()
    hobby = HobbySerializer()
    character = CharacterSerializer()
    additional_info = AdditionalInfoSerializer()
    baggage = BaggageSerializer()

    class Meta:
        model = Personage
        fields = (
            "id",
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


class PersonageRegenerateSerializer(serializers.Serializer):
    characteristic_type = serializers.ChoiceField(choices=TypeCharacteristic.choices)


class CharacteristicVisibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicVisibility
        fields = ("id", "uuid", "characteristic_type", "is_hidden")

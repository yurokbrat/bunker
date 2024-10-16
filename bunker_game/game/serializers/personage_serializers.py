from rest_framework import serializers

from bunker_game.game.models import Personage, Disease, Profession, Phobia, Hobby, Character, AdditionalInfo, Baggage
from bunker_game.users.serializers import UserSerializer


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ("name", "degree", "is_curable")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("name", "experience")


class PhobiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phobia
        fields = ("name", "stage")


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ("name", "experience")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("name",)


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ("name",)


class BaggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ("name", "status")


class PersonageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
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

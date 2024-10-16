from django.contrib import admin
from unfold.admin import ModelAdmin

from bunker_game.game.models import Catastrophe, Card, Personage, Bunker, BunkerRoom, Disease, Hobby, Phobia, \
    Profession, Baggage, Character, AdditionalInfo


@admin.register(Catastrophe)
class CatastropheAdmin(ModelAdmin): ...


@admin.register(Card)
class CardAdmin(ModelAdmin):
    list_filter = ("type",)


@admin.register(BunkerRoom)
class BunkerRoomAdmin(ModelAdmin): ...


@admin.register(Bunker)
class BunkerAdmin(ModelAdmin): ...


@admin.register(Disease)
class DiseaseAdmin(ModelAdmin): ...


@admin.register(Hobby)
class HobbyAdmin(ModelAdmin): ...


@admin.register(Phobia)
class PhobiaAdmin(ModelAdmin): ...


@admin.register(Profession)
class ProfessionAdmin(ModelAdmin): ...


@admin.register(Baggage)
class BaggageAdmin(ModelAdmin): ...


@admin.register(Character)
class CharacterAdmin(ModelAdmin): ...


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(ModelAdmin): ...


@admin.register(Personage)
class PersonageAdmin(ModelAdmin): ...

from django.contrib import admin
from unfold.admin import ModelAdmin

from bunker_game.game.models import (
    ActionCard,
    AdditionalInfo,
    Baggage,
    Bunker,
    BunkerRoom,
    Catastrophe,
    Character,
    Disease,
    Game,
    Hobby,
    Personage,
    Phobia,
    Profession,
)


@admin.register(Catastrophe)
class CatastropheAdmin(ModelAdmin): ...


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


@admin.register(ActionCard)
class ActionCardAdmin(ModelAdmin): ...


@admin.register(Game)
class GameAdmin(ModelAdmin): ...

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
class CatastropheAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Catastrophe.objects.filter(is_generated=False)


@admin.register(BunkerRoom)
class BunkerRoomAdmin(ModelAdmin): ...


@admin.register(Bunker)
class BunkerAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Bunker.objects.filter(is_generated=False)


@admin.register(Disease)
class DiseaseAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Disease.objects.filter(is_generated=False)


@admin.register(Hobby)
class HobbyAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Hobby.objects.filter(is_generated=False)


@admin.register(Phobia)
class PhobiaAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Phobia.objects.filter(is_generated=False)


@admin.register(Profession)
class ProfessionAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Profession.objects.filter(is_generated=False)


@admin.register(Baggage)
class BaggageAdmin(ModelAdmin):
    ordering = ("name",)

    def get_queryset(self, request):
        return Baggage.objects.filter(is_generated=False)


@admin.register(Character)
class CharacterAdmin(ModelAdmin):
    ordering = ("name",)


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(ModelAdmin):
    ordering = ("name",)


@admin.register(Personage)
class PersonageAdmin(ModelAdmin): ...


@admin.register(ActionCard)
class ActionCardAdmin(ModelAdmin): ...


@admin.register(Game)
class GameAdmin(ModelAdmin): ...

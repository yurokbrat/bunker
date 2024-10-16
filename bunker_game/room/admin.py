from django.contrib import admin
from unfold.admin import ModelAdmin

from bunker_game.room.models import Room


@admin.register(Room)
class CharacterAdmin(ModelAdmin): ...

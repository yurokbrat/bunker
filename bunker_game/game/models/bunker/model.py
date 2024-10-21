from django.db import models

from bunker_game.game.models.bunker.bunker_room import BunkerRoom
from bunker_game.utils.generate_hide_name import upload_to_bunkers


class Bunker(models.Model):
    name = models.CharField(max_length=120, verbose_name="название", unique=True)
    description = models.CharField(
        max_length=120,
        verbose_name="описание бункера",
        blank=True,
    )
    image = models.ImageField(
        upload_to=upload_to_bunkers,
        verbose_name="фотография",
        null=True,
        blank=True,
    )
    rooms = models.ManyToManyField(BunkerRoom, verbose_name="комнаты")

    class Meta:
        verbose_name = "бункер"
        verbose_name_plural = "бункеры"

    def __str__(self):
        return self.name

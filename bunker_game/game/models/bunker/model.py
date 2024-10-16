from django.db import models

from bunker_game.game.models.bunker.bunker_room import BunkerRoom


class Bunker(models.Model):
    name = models.CharField(max_length=120, verbose_name="название", unique=True)
    rooms = models.ManyToManyField(BunkerRoom, verbose_name="комнаты")

    class Meta:
        verbose_name = "бункер"
        verbose_name_plural = "бункеры"

    def __str__(self):
        return self.name

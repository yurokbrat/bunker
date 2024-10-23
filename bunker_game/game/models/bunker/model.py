import uuid

from django.db import models

from bunker_game.game.models.bunker.bunker_room import BunkerRoom
from bunker_game.utils.generate_hide_name import upload_to_bunkers


class Bunker(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, verbose_name="название")
    description = models.CharField(
        max_length=120,
        verbose_name="описание бункера",
        blank=True,
        default="",
    )
    image = models.ImageField(
        upload_to=upload_to_bunkers,
        verbose_name="фотография",
        null=True,
        blank=True,
    )
    rooms = models.ManyToManyField(BunkerRoom, blank=True, verbose_name="комнаты")
    is_generated = models.BooleanField(default=False, verbose_name="сгенерирован")

    class Meta:
        verbose_name = "бункер"
        verbose_name_plural = "бункеры"

    def __str__(self) -> str:
        return self.name

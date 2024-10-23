import uuid

from django.db import models


class BunkerRoom(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(
        max_length=100,
        verbose_name="название комнаты",
        unique=True,
    )
    area = models.PositiveSmallIntegerField(verbose_name="площадь комнаты в м²")

    class Meta:
        verbose_name = "комната бункера"
        verbose_name_plural = "комнаты бункеров"

    def __str__(self) -> str:
        return self.name

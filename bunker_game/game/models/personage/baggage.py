import uuid

from django.db import models

from bunker_game.game.constants import StatusBaggageChoice


class Baggage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, verbose_name="название")
    status = models.CharField(
        choices=StatusBaggageChoice.choices,
        max_length=50,
        verbose_name="состояние",
        blank=True,
        default="",
    )
    is_generated = models.BooleanField(default=False, verbose_name="сгенерирована")

    class Meta:
        verbose_name = "багаж"
        verbose_name_plural = "багажи"

    def __str__(self):
        return f"{self.name}"

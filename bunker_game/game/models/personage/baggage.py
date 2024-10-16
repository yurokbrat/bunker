from django.db import models

from bunker_game.game.models.constants import StatusBaggageChoice


class Baggage(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="название")
    status = models.CharField(
        choices=StatusBaggageChoice.choices,
        max_length=50,
        verbose_name="состояние",
    )

    class Meta:
        verbose_name = "багаж"
        verbose_name_plural = "багажи"

    def __str__(self):
        return self.name

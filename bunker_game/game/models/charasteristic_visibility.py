from django.db import models

from bunker_game.game.constants import TypeCharacteristic
from bunker_game.game.models.personage.model import Personage


class CharacteristicVisibility(models.Model):
    personage = models.ForeignKey(
        Personage,
        on_delete=models.CASCADE,
        related_name="visibility",
        verbose_name="персонаж",
    )
    characteristic_type = models.CharField(
        max_length=30,
        choices=TypeCharacteristic.choices,
        verbose_name="тип характеристики",
    )
    is_hidden = models.BooleanField(default=True, verbose_name="скрыта")

    class Meta:
        unique_together = ("personage", "characteristic_type")

    def __str__(self):
        return f"{self.personage} - {self.characteristic_type}"

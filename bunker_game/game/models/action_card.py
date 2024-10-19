from django.db import models

from bunker_game.game.constants import ActionCardTargetChoice


class ActionCard(models.Model):
    name = models.CharField(max_length=120, verbose_name="название")
    description = models.CharField(max_length=120, verbose_name="описание", blank=True, null=True)
    target = models.CharField(max_length=30, choices=ActionCardTargetChoice.choices, verbose_name="цель", blank=True, null=True)

    class Meta:
        verbose_name = "карта действия"
        verbose_name_plural = "карты действия"

    def __str__(self):
        return self.name


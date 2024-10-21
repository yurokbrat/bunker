from django.db import models

from bunker_game.game.constants import PhobiaStageChoice


class Phobia(models.Model):
    name = models.CharField(max_length=120, verbose_name="название")
    stage = models.CharField(
        max_length=120,
        choices=PhobiaStageChoice.choices,
        verbose_name="стадия",
        blank=True,
    )

    class Meta:
        verbose_name = "фобия"
        verbose_name_plural = "фобии"

    def __str__(self):
        return f"{self.name} - {self.stage}"

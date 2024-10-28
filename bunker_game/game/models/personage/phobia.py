import uuid

from django.db import models

from bunker_game.game.enums import PhobiaStageChoice


class Phobia(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, verbose_name="название")
    stage = models.CharField(
        max_length=120,
        choices=PhobiaStageChoice.choices,
        verbose_name="стадия",
        blank=True,
        default="",
    )
    is_generated = models.BooleanField(default=False, verbose_name="сгенерирована")

    class Meta:
        verbose_name = "фобия"
        verbose_name_plural = "фобии"

    def __str__(self) -> str:
        return f"{self.name}"

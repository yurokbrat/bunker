import uuid

from django.db import models

from bunker_game.game.constants import ActionCardTargetChoice


class ActionCard(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, verbose_name="название")
    key = models.SlugField(max_length=50, verbose_name="ключ карты")
    description = models.CharField(
        max_length=120,
        verbose_name="описание",
        blank=True,
    )
    target = models.CharField(
        max_length=30,
        choices=ActionCardTargetChoice.choices,
        verbose_name="цель",
        blank=True,
    )

    class Meta:
        verbose_name = "карта действия"
        verbose_name_plural = "карты действия"

    def __str__(self) -> str:
        return self.name

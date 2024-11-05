import uuid

from django.db import models

from bunker_game.game.models import ActionCard


class ActionCardUsage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    card = models.OneToOneField(
        ActionCard,
        on_delete=models.CASCADE,
        verbose_name="карта",
    )
    personage = models.ForeignKey(
        "game.Personage",
        on_delete=models.SET_NULL,
        related_name="action_cards",
        null=True,
        blank=True,
        verbose_name="персонаж",
    )
    game = models.ForeignKey(
        "game.Game",
        on_delete=models.SET_NULL,
        related_name="action_cards",
        null=True,
        blank=True,
        verbose_name="игра",
    )
    is_used = models.BooleanField(default=False, verbose_name="использована")

    class Meta:
        verbose_name = "использование карты действия"
        verbose_name_plural = "использования карт действий"

    def __str__(self) -> str:
        return f"{self.card} - {self.personage} - {self.game}"

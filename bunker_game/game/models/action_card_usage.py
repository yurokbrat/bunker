import uuid

from django.db import models

from bunker_game.game.models import Game, Personage
from bunker_game.game.models.action_card import ActionCard


class ActionCardUsage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    card = models.OneToOneField(
        ActionCard,
        on_delete=models.CASCADE,
        verbose_name="карта",
    )
    personage = models.ForeignKey(
        Personage,
        on_delete=models.SET_NULL,
        related_name="action_cards",
        null=True,
        blank=True,
        verbose_name="персонаж",
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.SET_NULL,
        related_name="action_cards",
        null=True,
        blank=True,
        verbose_name="игра",
    )
    is_used = models.BooleanField(default=False, verbose_name="использована")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("personage", "game", "card"),
                name="unique_personage_game_action_card",
            ),
            models.UniqueConstraint(
                fields=("personage", "card"),
                name="unique_personage_action_card",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.card} - {self.personage} - {self.game}"

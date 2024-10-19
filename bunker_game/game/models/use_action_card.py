from django.db import models

from bunker_game.game.models import Personage, Game
from bunker_game.game.models.action_card import ActionCard


class UseActionCard(models.Model):
    card = models.OneToOneField(ActionCard, on_delete=models.CASCADE, verbose_name="карта")
    personage = models.ForeignKey(Personage, on_delete=models.SET_NULL, related_name="action_cards", null=True,
                                  blank=True, verbose_name="персонаж")
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, related_name="action_cards", null=True, blank=True,
                             verbose_name="игра")
    is_used = models.BooleanField(default=False, verbose_name="использована")

    class Meta:
        unique_together = ("card", "personage", "game")

    def __str__(self):
        return f"{self.card} - {self.personage} - {self.game}"
